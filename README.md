# AI Seminar 2026 — 대화에서 실행으로

챗팅 → 바이브 코딩 → 에이전트 → 에이전틱 워크로 이어지는 AI 세미나 시리즈입니다.

- **메인 허브**: https://waterfirst.github.io/ai-seminar-2026/
- **4차 최신판**: https://waterfirst.github.io/ai-seminar-2026/fourth-seminar-2026.html
- **최신 검증일**: 2026-08-18

## 세미나 순서

| 차수 | 주제 | 날짜 | 파일 |
|---|---|---:|---|
| 1차 | AI가 바꾸는 연구개발 | 2026-06-13 | [`index2.html`](./index2.html) |
| 2차 | 지금 당장 실무에 쓸 수 있는 AI 도구 완전 가이드 | 2026-06 | [`index1.html`](./index1.html) |
| 3차 | 토큰을 아끼는 AI 에이전트 운영 전략 | 2026-07 | [`token-frugal-agent-playbook-2026.html`](./token-frugal-agent-playbook-2026.html) |
| 4차 | AGI로 가는 길목, Agentic Work | 2026-08-18 | [`fourth-seminar-2026.html`](./fourth-seminar-2026.html) |

> 2차 자료는 삭제된 것이 아닙니다. 초기 파일명 재배치 때문에 **1차가 `index2.html`, 2차가 `index1.html`**로 저장되어 있었습니다. 루트 허브에서 올바른 순서로 다시 연결했습니다.
>
> 2차와 3차 발표 페이지의 기존 접속 코드는 `1111`입니다. 메인 허브와 4차 최신판은 바로 열립니다.

## 4차 세미나 구성

- Chat → Vibe Coding → Agent → Agentic Work 진화 과정
- AGI에 대한 과장 없는 능력 단계 구분
- Model, Context, Skills, Tools, Orchestration, Governance 스택
- Skills, MCP 2026-07-28, A2A v1.0, Computer Use, Memory, Evals
- Stanford AI Index 2026, Microsoft WTI 2026, METR 최신 데이터
- OLED/TFT 신뢰성 분석을 예로 든 제조·연구개발 멀티에이전트 구조
- 자율성·도구 권한·사람 검토·에이전트 수를 조절하는 교육용 시뮬레이터
- 대한민국 AI 기본법, KISA·NSA 지침 기반 에이전트 보안
- 30일 도입 로드맵

## 편집 원칙

- 1·2·3차 본문은 발표 당시의 기록으로 보존합니다.
- 빠르게 바뀌는 모델명·시장 정보는 4차 최신판에서 공식·원문 자료로 다시 검증합니다.
- 최신 데이터와 과거 발표 내용을 혼동하지 않도록 각 기존 페이지에 아카이브 안내를 표시합니다.
- 정적 GitHub Pages에서 별도 빌드 없이 실행되며 모바일·다크/라이트·인쇄를 지원합니다.

## 주요 파일

```text
ai-seminar-2026/
├── index.html                              # 4부작 메인 허브
├── index2.html                             # 1차 세미나
├── index1.html                             # 2차 세미나
├── token-frugal-agent-playbook-2026.html   # 3차 메인 본편
├── claude-masterclass-2026.html            # 3차 확장자료
├── index3.html                             # 3차 구버전 아카이브
├── fourth-seminar-2026.html                # 4차 최신판 + 시뮬레이터
├── PLAN.md                                 # 이번 개편 목적·완료 조건
├── AGENTS.md                               # 저장소 작업 규칙
├── images/                                 # 1·3차 이미지
├── img/                                    # 2차 이미지
├── backend/                                # 기존 FastAPI 실습
└── frontend/                               # 기존 Streamlit 실습
```

## 최신 근거 자료

- [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI — Agents SDK](https://developers.openai.com/api/docs/guides/agents)
- [OpenAI — Using tools](https://developers.openai.com/api/docs/guides/tools)
- [Stanford HAI — The 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- [Microsoft — 2026 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)
- [METR — Task-Completion Time Horizons](https://metr.org/time-horizons/)
- [MCP — 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [A2A Protocol — Version 1.0](https://a2a-protocol.org/latest/announcing-1.0/)
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)
- [KISA — AI 보안 위협 대응 매뉴얼](https://www.kisa.or.kr/401/form?postSeq=3712)
- [국가법령정보센터 — 인공지능 기본법](https://www.law.go.kr/lsInfoP.do?lsId=014820)

## 로컬 확인

정적 파일이므로 저장소 루트에서 간단한 HTTP 서버로 확인할 수 있습니다.

```bash
python -m http.server 8000
```

브라우저에서 `http://localhost:8000/`을 엽니다.
