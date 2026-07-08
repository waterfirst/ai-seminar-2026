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