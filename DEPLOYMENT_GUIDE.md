# 🚀 사내 GPT 엔터프라이즈 배포 가이드

## 빠른 시작 (5분)

### 로컬 환경 (개발/테스트용)

#### 1️⃣ 환경 설정
```bash
# 1. 저장소 클론 후 디렉토리 진입
cd ai-seminar-2026

# 2. .env 파일 생성 (OpenAI API 키 입력)
cp .env.example .env
# 편집: OPENAI_API_KEY=sk-xxxx (실제 키 입력)
```

#### 2️⃣ 백엔드 실행
```bash
# 2-1. 패키지 설치
cd backend
pip install -r requirements.txt

# 2-2. 백엔드 서버 시작
python main.py

# 출력:
# 📡 FastAPI 백엔드 시작 (http://localhost:8000)
# 📖 API 문서: http://localhost:8000/docs
```

#### 3️⃣ 프런트엔드 실행 (새 터미널)
```bash
# 3-1. 패키지 설치
cd frontend
pip install -r requirements.txt

# 3-2. Streamlit 앱 시작
streamlit run app.py

# 브라우저 자동 오픈: http://localhost:8501
```

#### 4️⃣ 테스트
- **프런트**: http://localhost:8501 에서 질문 입력 → 응답 확인
- **백엔드 API**: http://localhost:8000/docs에서 Swagger UI로 테스트

---

## 도커 배포 (프로덕션)

### 사전 준비
- Docker & Docker Compose 설치 (Mac/Windows: Docker Desktop, Linux: `apt install docker.io`)
- `.env` 파일 생성 (OpenAI API 키 포함)

### 배포 명령어
```bash
# 1. 이미지 빌드 + 컨테이너 실행
docker-compose up -d

# 2. 실행 상태 확인
docker-compose ps
# 출력:
# NAME                COMMAND                  STATUS
# gpt-backend         "python main.py"         Up (healthy)
# gpt-frontend        "streamlit run app.py"   Up

# 3. 로그 확인
docker-compose logs -f gpt-backend
docker-compose logs -f gpt-frontend

# 4. 중지
docker-compose down
```

### 배포 후 접속
- **프런트**: http://your-server-ip (포트 80)
- **백엔드 API**: http://your-server-ip:8000/docs

---

## 폴더 구조 및 파일 설명

```
ai-seminar-2026/
├── backend/
│   ├── main.py                    # FastAPI 백엔드 메인 코드
│   ├── requirements.txt            # Python 패키지 목록
│   ├── Dockerfile                  # Docker 설정
│   └── data/                       # SQLite DB 파일 저장 위치
├── frontend/
│   ├── app.py                      # Streamlit 앱 코드
│   ├── requirements.txt            # Python 패키지 목록
│   └── Dockerfile                  # Docker 설정
├── docker-compose.yml              # Docker Compose 통합 설정
├── .env.example                    # 환경변수 템플릿
├── web_db_gpt_guide.md            # 개념 설명 (이 문서)
└── DEPLOYMENT_GUIDE.md            # 배포 가이드 (지금 읽는 문서)
```

---

## API 명세

### 1. 질문 → 응답 (`POST /ask-gpt`)

**요청:**
```json
{
  "user_query": "어제 불량률 요약해줄래?"
}
```

**응답:**
```json
{
  "user_query": "어제 불량률 요약해줄래?",
  "gpt_response": "어제 주요 라인의 불량률은...",
  "timestamp": "2026-06-26T14:30:00.123456"
}
```

**cURL 예제:**
```bash
curl -X POST "http://localhost:8000/ask-gpt" \
  -H "Content-Type: application/json" \
  -d '{"user_query": "어제 불량률 요약해줄래?"}'
```

### 2. 대화 이력 조회 (`GET /history`)

**요청:**
```bash
curl "http://localhost:8000/history?limit=10"
```

**응답:**
```json
{
  "count": 5,
  "conversations": [
    {
      "id": 5,
      "user_query": "...",
      "gpt_response": "...",
      "timestamp": "2026-06-26T14:30:00"
    }
  ]
}
```

### 3. 헬스 체크 (`GET /`)

```bash
curl "http://localhost:8000/"
# {"status": "ok", "message": "사내 GPT 백엔드 실행 중"}
```

---

## 트러블슈팅

### ❌ 백엔드 연결 실패
```
🔌 백엔드 연결 실패. 백엔드가 실행 중인지 확인하세요.
```
**해결:**
- 백엔드가 `python main.py`로 실행 중인지 확인
- 방화벽이 포트 8000을 차단하지 않는지 확인
- API URL 확인 (로컬: http://localhost:8000, 도커: http://gpt-backend:8000)

### ❌ OpenAI API 오류
```
❌ GPT 응답 실패: Error: Invalid API key
```
**해결:**
- `.env` 파일에 `OPENAI_API_KEY`를 올바르게 설정했는지 확인
- API 키가 유효한지 확인 (https://platform.openai.com/api-keys)
- API 키에 사용 가능한 크레딧이 있는지 확인

### ❌ 포트 충돌
```
Error: Address already in use: ('0.0.0.0', 8000)
```
**해결:**
```bash
# 포트 8000을 사용 중인 프로세스 확인
lsof -i :8000

# 프로세스 종료 (PID 확인 후)
kill -9 <PID>
```

### ❌ 도커 빌드 실패
```bash
# 이미지 캐시 제거 후 다시 빌드
docker-compose down
docker system prune -a
docker-compose up -d --build
```

---

## 다음 단계

### [Step 4] PostgreSQL 연동 (프로덕션)
- SQLite → PostgreSQL 마이그레이션
- 환경변수 변경: `DATABASE_URL=postgresql://user:pwd@host/db`
- `docker-compose.yml`에 PostgreSQL 서비스 추가

### [Step 5] RAG 시스템 구축 (사내 문서 기반 GPT)
- 사내 가이드/보고서 PDF → Vector DB (ChromaDB)
- LangChain으로 문서 검색 + 답변 생성
- `/ask-gpt` 엔드포인트에 문서 검색 기능 통합

### [Step 6] 인증 & 로깅
- JWT 토큰 기반 사용자 인증
- 사용자별 대화 이력 분리
- API 호출 로깅 및 모니터링

---

## 참고 링크

- **FastAPI 공식 문서**: https://fastapi.tiangolo.com
- **Streamlit 공식 문서**: https://docs.streamlit.io
- **OpenAI API 문서**: https://platform.openai.com/docs
- **Docker 가이드**: https://docs.docker.com

---

**문제가 발생하면:**
- 터미널 로그 확인: `docker-compose logs -f`
- GitHub Issues 등록 (조직 내 문의)
- Claude와 상담: "Step 5: 사내 RAG 시스템 구축해 줄래?" 등

**마지막 점검:**
- [ ] `.env` 파일 생성 & OPENAI_API_KEY 입력
- [ ] `docker-compose up -d` 실행
- [ ] 프런트 http://localhost (또는 http://server-ip) 접속 확인
- [ ] 질문 입력 → 응답 확인
