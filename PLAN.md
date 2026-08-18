# AI Seminar Series Hub and Fourth Seminar

## 목적

- 루트 URL을 1·2·3차 세미나를 한눈에 찾는 시리즈 허브로 복원한다.
- 누락된 것으로 보였던 2차 자료(`index1.html`)의 위치를 명확히 표시한다.
- 2026-08-18 기준으로 검증한 최신 에이전틱 AI 기술을 4차 세미나로 추가한다.

## 입력

- 1차: `index2.html`
- 2차: `index1.html`
- 3차: `token-frugal-agent-playbook-2026.html`
- 기존 디자인·운영 규칙: `AGENTS.md`, `DESIGN_REFERENCE.md`, `README.md`
- 최신 근거: OpenAI 공식 문서, Stanford AI Index 2026, Microsoft WTI 2026,
  METR, MCP/A2A 공식 규격, NSA/KISA 보안 지침, 대한민국 AI 기본법

## 산출물

- `index.html`: 공개용 시리즈 메인 허브
- `fourth-seminar-2026.html`: 4차 세미나 발표 페이지 및 자율성 시뮬레이터
- 1·2·3차 페이지의 허브/최신판 이동 링크
- 최신 파일 구조와 출처를 반영한 `README.md`

## 제약

- 과거 발표 내용은 당시 자료로 보존하고, 최신 사실은 허브와 4차에서 갱신한다.
- 외부 발표에서 사내 비밀·계정·비밀번호를 노출하지 않는다.
- 정적 GitHub Pages에서 별도 빌드 없이 동작해야 한다.
- 모바일, 키보드 탐색, 인쇄를 지원한다.

## 완료 조건

- 루트에서 네 세미나가 올바른 순서와 링크로 보인다.
- 2차가 `index1.html`로 명확히 식별된다.
- 4차 페이지의 탐색, 테마, 진행률, 시뮬레이터가 오류 없이 동작한다.
- 내부 상대 링크와 HTML 문법 검증을 통과한다.
- 변경 내용을 분리 브랜치에 커밋하고 GitHub에 게시한다.
