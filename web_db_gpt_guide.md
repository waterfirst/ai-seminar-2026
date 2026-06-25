# [실습 핸드북] 프런트/백엔드·DB 핵심 정리 및 사내 GPT 엔터프라이즈 단계별 구현 가이드

## 📌 1. 프런트엔드 & 백엔드 종류 및 특징

웹 서비스는 크게 사용자 눈에 보이는 프런트엔드와 뒷단에서 연산·보안을 담당하는 백엔드로 나뉩니다.

### 🖥️ 프런트엔드 (Frontend): 사용자가 보는 화면

* **HTML/CSS/JS (순수 웹)**: 가장 기본이 되는 뼈대(HTML), 인테리어(CSS), 움직임(JS)입니다. 가볍지만 복잡한 화면을 짜기엔 코드가 스파게티처럼 꼬입니다.
* **React / Vue / Angular (프레임워크)**: 레고 블록처럼 화면을 '컴포넌트(부품)' 단위로 쪼개어 조립하는 현대적 방식입니다. 화면 전환이 부드럽고 시뮬레이션 UI에 유리하지만, Vite 같은 빌드(압축) 도구 공부가 필요해 러닝 커브가 높습니다.
* **R Shiny / Streamlit (대시보드형 프런트)**: **(강력 추천)** 프런트엔드 언어를 몰라도 R이나 Python 코드만으로 화면 레이아웃을 알아서 그려주는 고마운 도구입니다.

### ⚙️ 백엔드 (Backend): 눈에 안 보이는 비즈니스 로직 및 연산

* **FastAPI (Python)**: 현재 가장 트렌디한 도구입니다. 가볍고 속도가 압도적으로 빠르며, AI/GPT 관련 파이썬 라이브러리(LangChain 등)를 접목하기 가장 좋습니다. 데이터 규격 검증(Pydantic)과 API 문서 자동 생성이 강력합니다.
* **R (Plumber)**: R 코드를 백엔드 API 서버로 만들어주는 도구입니다. R로 짠 무거운 통계/시뮬레이션 로직이 이미 있다면 이를 백엔드로 서빙할 때 씁니다.
* **Express (Node.js) / Spring Boot (Java)**: 대규모 IT 서비스나 엔터프라이즈 시스템 구축에 쓰이는 전통적인 백엔드 스택입니다. 비프로그래머의 1인 개발용으로는 다소 무겁습니다.

## 🗄️ 2. 데이터베이스(DB) 종류 및 특징

사내 대시보드나 GPT 서비스를 만들 때 데이터를 어디에 어떻게 저장할지 결정해야 합니다.

### 📊 Relational DB (관계형 데이터베이스 - SQL)

* **종류**: PostgreSQL, MySQL, SQLite(파일 기반 가벼운 DB)
* **특징**: 엑셀 시트처럼 행(Row)과 열(Column)이 명확하게 정해진 표 형태입니다. 데이터 간의 관계(ID 연동 등)가 끈끈하고 정확성이 완벽해야 하는 업무(결재 시스템, 사용자 계정, 정형 가동 데이터 등)에 필수적입니다.
* **사내 추천**: 가볍게 실습할 때는 파일 하나로 끝나는 SQLite를 쓰고, 실제 배포할 때는 사내 서버에 PostgreSQL을 도커로 띄우는 것이 좋습니다.

### 📝 NoSQL / Document DB (비관계형 데이터베이스)

* **종류**: MongoDB, Redis(초고속 메모리 DB)
* **특징**: 고정된 표 형태가 아니라 자유로운 형태(JSON 메모장 형식)로 데이터를 저장합니다. GPT 대화 이력처럼 길이가 제각각이고 형태가 계속 바뀌는 데이터를 빠르게 쌓고 읽을 때 유리합니다.

### 📐 Vector DB (벡터 데이터베이스 - AI 특화)

* **종류**: ChromaDB, FAISS, Pinecone, pgvector(PostgreSQL 확장)
* **특징**: 사내 가이드라인, 보고서 PDF 같은 텍스트를 AI가 이해할 수 있는 수학적 좌표(Vector Embedded)로 바꾸어 저장하는 DB입니다. 사내 문서 기반 GPT(RAG 시스템)를 만들 때 핵심이 됩니다.

## 🚀 3. 사내 GPT 엔터프라이즈 단계별 실습 가이드

### 📦 전체 아키텍처 다이어그램

```
┌─────────────────────────────────────┐
│  User Browser (80포트)               │
│  R Shiny / Streamlit GUI             │
└──────────────┬──────────────────────┘
               │ HTTP Request (JSON)
               ▼
┌─────────────────────────────────────┐
│  FastAPI Backend (8000포트)          │
│  - Route: /ask-gpt (POST)            │
│  - 사용자 질문 → OpenAI API 호출      │
│  - 응답 → DB 저장                    │
└──────────────┬──────────────────────┘
               │ SQL Query / Document Store
               ▼
┌─────────────────────────────────────┐
│  Database Layer                      │
│  - PostgreSQL (구조화 데이터)        │
│  - MongoDB (GPT 대화 이력)          │
│  - ChromaDB (임베딩 저장)            │
└─────────────────────────────────────┘
```

### 🔧 단계별 구현 가이드

#### [1단계] FastAPI 백엔드 기초
- 목표: "/ask-gpt" 엔드포인트 구현
- 파일: `backend/main.py`
- 기능:
  - 사용자 질문 수신 → OpenAI API 호출
  - 응답 저장 (SQLite 또는 PostgreSQL)
  - JSON 형태로 프런트에 반환

**예시 코드 구조**:
```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class Question(BaseModel):
    user_query: str

@app.post("/ask-gpt")
async def ask_gpt(q: Question):
    # OpenAI API 호출
    # DB에 저장
    # 응답 반환
    pass
```

#### [2단계] Streamlit 프런트엔드 기초
- 목표: 간단한 채팅 UI 구성
- 파일: `frontend/app.py`
- 기능:
  - 텍스트 입력창 (st.text_input)
  - 백엔드 "/ask-gpt" API 호출
  - 응답 결과 표시

**예시 코드 구조**:
```python
# app.py (Streamlit)
import streamlit as st
import requests

st.title("사내 GPT 챗봇")

user_input = st.text_input("질문을 입력하세요:")
if user_input:
    response = requests.post(
        "http://localhost:8000/ask-gpt",
        json={"user_query": user_input}
    )
    st.write(response.json())
```

#### [3단계] 데이터베이스 연동
- SQLite (개발용): 파일 1개로 관리 → 배포 전 테스트
- PostgreSQL (실제 배포): 사내 서버에 도커로 설치

**예시**:
```python
# SQLite 초기화
import sqlite3
conn = sqlite3.connect("gpt_history.db")
cursor = conn.cursor()
cursor.execute("""
  CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY,
    user_query TEXT,
    gpt_response TEXT,
    timestamp DATETIME
  )
""")
conn.commit()
```

#### [4단계] Docker로 통합 배포
- `docker-compose.yml`로 백엔드 + 프런트엔드 한 번에 띄우기

**예시 docker-compose.yml**:
```yaml
version: '3'
services:
  gpt-backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=sqlite:///./gpt_history.db
    restart: always

  gpt-frontend:
    build: ./frontend
    ports:
      - "80:3838"  # 사내 사용자들이 IP 주소만 치면 80포트로 바로 진입
    depends_on:
      - gpt-backend
    restart: always
```

### 💡 AI를 활용한 실습 팁 (바이브 리뷰)

**준비 완료! Claude 대화창에서 이렇게 명령하세요:**

> "나는 R 파워 유저이자 비프로그래머입니다. 공유된 가이드라인을 바탕으로 사내 GPT 엔터프라이즈 앱을 만들고 싶어요. **[1단계] 기초 API 연동을 위한 FastAPI 백엔드 코드(main.py)**부터 짜줘요. 복잡하지 않고 에러 가능성이 없는 안전장치 코드를 포함해 주세요."

**그 다음:**

> "[2단계] 이제 Streamlit 프런트엔드(app.py)를 위 백엔드와 연동해 줘요. 간단한 채팅 UI로 백엔드 API를 호출하는 구조를 원해요."

**마지막:**

> "[3단계] SQLite 데이터베이스 초기화 및 대화 이력 저장 로직을 추가해 줘요. 사용자 질문과 GPT 응답이 타임스탬프와 함께 저장되도록."

---

**작성자**: 비프로그래머 분석가(R 파워 유저) 관점  
**목표**: 개념적 구조 이해 → AI와 함께 단계별 조립  
**대상**: AI 3차 세미나 참가자  
**최종 산출물**: 실행 가능한 로컬 앱 + Docker 배포 파일
