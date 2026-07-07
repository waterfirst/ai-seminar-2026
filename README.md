# 삼성디스플레이 품질팀 AI 세미나 시리즈

삼성디스플레이 품질팀 실무자 대상 AI 실무 교육 자료 모음입니다.

🔗 **메인 (3차 세미나 본편)**: https://waterfirst.github.io/ai-seminar-2026/

---

## 세미나 자료 목록

### 3차 세미나 본편 — Claude Code 심화 & 토큰 최적화 (2026.07) `index.html`
**대상**: 품질팀 실무자  
**링크**: https://waterfirst.github.io/ai-seminar-2026/  
**접속**: 비밀번호 `0000`

주요 내용:
- 토큰 비용 문제와 RTK(Rust Token Killer) 훅 시스템
- Claude Code Hooks 설정 (PreToolUse / PostToolUse)
- CLAUDE.md 작성법과 메모리 파일 관리
- AI 에이전트 운영 5원칙 (VFF · 마지막 1cm · 토큰 설계)
- 실전 절약 측정: `rtk gain` 명령 활용

---

### 1차 세미나 — AI가 바꾸는 연구개발 (2026.05) `index2.html`
**대상**: SDC 연구소 재료연구팀 연구원  
**링크**: https://waterfirst.github.io/ai-seminar-2026/index2.html

주요 내용:
- 글로벌 AI 현황 및 기업 도입 사례
- Gemini · Claude · ChatGPT 비교 분석
- 연구개발 실무 적용 방법
- AI 도구 실습 가이드

---

### 사례 연구 — 프롬프트로 머신러닝하기 `ml-with-prompts.html`
**링크**: https://waterfirst.github.io/ai-seminar-2026/ml-with-prompts.html

코딩 없이 Claude 프롬프트만으로 머신러닝을 구현한 실제 사례 연구.  
특성 중요도 분석, 교차 검증, 앙상블 모델 구현 과정 포함.

---

### AWE USA 2026 출장 보고서 `awe_report.html`
**링크**: https://waterfirst.github.io/ai-seminar-2026/awe_report.html

Long Beach 전시회 AR/XR 기술 트렌드 현장 정리.  
AWE 센싱 교육 자료 및 주요 전시 부스 분석.

---

## 파일 구조

```
ai-seminar-2026/
├── index.html        # 3차 세미나 본편 — Claude Code 심화 & 토큰 최적화 (비밀번호: 0000)
├── index2.html       # 1차 세미나 — AI가 바꾸는 연구개발
├── claude-masterclass-2026.html   # 3차 확장자료(어두운 톤)
├── token-frugal-agent-playbook-2026.html   # 3차 보강자료(밝은 톤)
├── index3.html       # 3차 구버전/중복 후보
├── ml-with-prompts.html    # ML + 프롬프트 사례 연구
├── awe_report.html         # AWE 2026 출장 보고서
├── zoom_guide.html         # Zoom 사용 가이드
├── ai-research-verification-2026.html
├── etf-investment-ai.html
├── images/           # 1차 세미나 이미지
└── img/              # 2차 세미나 이미지
```

---

## 관련 저장소

- [awe_2026_LA](https://github.com/waterfirst/awe_2026_LA) — AWE 2026 출장 원본 자료

## 3차 세미나 추가 자료

### 📌 3차 세미나 페이지 구조 요약
- **본편(메인)**: `index.html`
- **확장자료(어두운 톤)**: `claude-masterclass-2026.html`
- **보강자료(밝은 톤)**: `token-frugal-agent-playbook-2026.html`
- **구버전/정리 대상**: `index3.html`

### 📚 실습 핸드북
- **[web_db_gpt_guide.md](./web_db_gpt_guide.md)** — 프런트/백엔드·DB 핵심 정리 및 사내 GPT 엔터프라이즈 단계별 구현 가이드
  - 프런트엔드 (HTML/CSS/JS, React, R Shiny, Streamlit)
  - 백엔드 (FastAPI 추천, Express/Spring Boot)
  - 데이터베이스 (SQL, NoSQL, Vector DB)
  - 사내 GPT 엔터프라이즈 Step 1-4 실습 가이드

- **[DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)** — 배포 & 운영 가이드
  - 로컬 개발 환경 5분 빠른 시작
  - Docker 프로덕션 배포
  - API 명세 및 트러블슈팅

- **[token-frugal-agent-playbook-2026.md](./token-frugal-agent-playbook-2026.md)** — 토큰을 아끼는 AI 에이전트 운영 전략
  - 회사 전체 토큰 부족 사태의 구조적 원인
  - 큰 모델/작은 모델/스크립트 분업 원칙
  - 메모리 설계, 루프 브레이크, fallback SOP
  - 3차 세미나 보강용 발표 골격과 체크리스트

- **[token-frugal-agent-playbook-2026.html](./token-frugal-agent-playbook-2026.html)** — 밝은 배경 기본의 세미나 발표용 페이지
  - 금단현상 카툰을 인트로 훅으로 배치
  - 토큰 누수 원인, 운영 원칙, 조직 실행안을 카드형으로 재구성
  - 임원/연구원 발표에 바로 쓸 수 있는 시각 자료

### 💻 실행 가능한 코드
- **backend/** — FastAPI 백엔드 (main.py + requirements.txt + Dockerfile)
  - POST /ask-gpt 엔드포인트
  - SQLite 데이터베이스 자동 초기화
  - OpenAI API 연동

- **frontend/** — Streamlit 프런트엔드 (app.py + requirements.txt + Dockerfile)
  - 채팅 UI (입력창 + 응답 표시)
  - 대화 이력 조회
  - 백엔드 헬스 체크

- **docker-compose.yml** — 한 번에 배포 가능한 통합 설정
- **.env.example** — 환경변수 템플릿 (OpenAI API 키 설정)

---

## 3차 — 클로드 특별강의
- `claude-masterclass-2026.html` : 3차 세미나 **확장자료**. Chat/Cowork/Code·MCP·키메라(클로드+GPT+제미나이)·에이전트 실전(실리콘네스트 구축)·스킬/헌법/키관리
