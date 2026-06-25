"""
FastAPI 백엔드 — 사내 GPT 엔터프라이즈 기초
Z AI 코더 (속도·안전장치·데이터 처리)

기능:
- POST /ask-gpt → 사용자 질문 → OpenAI API → DB 저장 → JSON 응답
- GET /history → 대화 이력 조회
- SQLite 자동 초기화 (배포 전 테스트용)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import sqlite3
import os
from datetime import datetime
import openai

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. 초기화 설정
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

app = FastAPI(
    title="사내 GPT 백엔드",
    description="기초 API 연동 (Step 1)",
    version="1.0"
)

# OpenAI API 키 (환경변수로만 읽기)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    print("⚠️  경고: OPENAI_API_KEY 환경변수를 설정하세요.")
    OPENAI_API_KEY = "dummy-key-for-test"  # 테스트용 더미 키

openai.api_key = OPENAI_API_KEY

# SQLite 설정
DB_FILE = "gpt_history.db"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. 데이터 모델
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Question(BaseModel):
    user_query: str = Field(..., min_length=1, max_length=1000, description="사용자 질문")

class Answer(BaseModel):
    user_query: str
    gpt_response: str
    timestamp: str

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. 데이터베이스 유틸리티
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def init_db():
    """SQLite 초기화 (테이블 없으면 자동 생성)"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # 테이블 생성 (없으면 무시)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_query TEXT NOT NULL,
                gpt_response TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()
        print(f"✅ DB 초기화 완료: {DB_FILE}")
    except Exception as e:
        print(f"❌ DB 초기화 실패: {e}")

def save_to_db(user_query: str, gpt_response: str):
    """대화 이력을 DB에 저장"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        timestamp = datetime.now().isoformat()
        cursor.execute(
            "INSERT INTO conversations (user_query, gpt_response, timestamp) VALUES (?, ?, ?)",
            (user_query, gpt_response, timestamp)
        )

        conn.commit()
        conn.close()
        print(f"✅ DB 저장 완료: {timestamp}")
    except Exception as e:
        print(f"❌ DB 저장 실패: {e}")

def get_history(limit: int = 10):
    """대화 이력 조회"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, user_query, gpt_response, timestamp FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,)
        )

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": row[0],
                "user_query": row[1],
                "gpt_response": row[2],
                "timestamp": row[3]
            }
            for row in rows
        ]
    except Exception as e:
        print(f"❌ DB 조회 실패: {e}")
        return []

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. API 엔드포인트
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_event("startup")
async def startup_event():
    """앱 시작 시 DB 초기화"""
    init_db()
    print("🚀 FastAPI 백엔드 시작")

@app.get("/")
async def root():
    """헬스 체크"""
    return {"status": "ok", "message": "사내 GPT 백엔드 실행 중"}

@app.post("/ask-gpt", response_model=Answer)
async def ask_gpt(q: Question):
    """
    사용자 질문 → OpenAI API 호출 → DB 저장 → 응답

    예시:
    ```
    curl -X POST "http://localhost:8000/ask-gpt" \
      -H "Content-Type: application/json" \
      -d '{"user_query": "코스피 분석 해줄래?"}'
    ```
    """

    user_query = q.user_query.strip()

    # 입력 유효성 검사
    if not user_query:
        raise HTTPException(status_code=400, detail="질문을 입력하세요.")

    # OpenAI API 호출 (안전장치)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "당신은 친절한 사내 어시스턴트입니다. 간결하고 정확하게 답변해주세요."
                },
                {
                    "role": "user",
                    "content": user_query
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        gpt_response = response["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"❌ OpenAI API 호출 실패: {e}")
        raise HTTPException(status_code=500, detail=f"GPT 응답 실패: {str(e)}")

    # DB에 저장
    save_to_db(user_query, gpt_response)

    # 응답 반환
    return Answer(
        user_query=user_query,
        gpt_response=gpt_response,
        timestamp=datetime.now().isoformat()
    )

@app.get("/history")
async def get_conversation_history(limit: int = 10):
    """대화 이력 조회"""
    history = get_history(limit)
    return {"count": len(history), "conversations": history}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. 실행
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    import uvicorn

    print("📡 FastAPI 백엔드 시작 (http://localhost:8000)")
    print("📖 API 문서: http://localhost:8000/docs")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
