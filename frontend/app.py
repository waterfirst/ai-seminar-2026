"""
Streamlit 프런트엔드 — 사내 GPT 엔터프라이즈 기초
GPT 코더 (UI/UX·완성도·문서화)

기능:
- 깔끔한 채팅 인터페이스 (입력창 + 질문 전송)
- 백엔드 API (/ask-gpt) 호출
- 실시간 응답 표시
- 대화 이력 탭

실행:
  streamlit run app.py
"""

import streamlit as st
import requests
import json
from datetime import datetime
from typing import Optional

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. 페이지 설정
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.set_page_config(
    page_title="사내 GPT 챗봇",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 사내 GPT 챗봇")
st.markdown("AI와 함께 업무를 효율화하세요.")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. 환경 설정
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 백엔드 API URL (로컬 또는 도커)
BACKEND_URL = "http://localhost:8000"
# 도커 환경에서: "http://gpt-backend:8000"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. 헬퍼 함수
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@st.cache_resource
def check_backend_health():
    """백엔드 헬스 체크"""
    try:
        response = requests.get(f"{BACKEND_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False

def ask_gpt(query: str) -> Optional[dict]:
    """백엔드 API에 질문 전송"""
    try:
        response = requests.post(
            f"{BACKEND_URL}/ask-gpt",
            json={"user_query": query},
            timeout=10
        )

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"❌ 백엔드 오류 ({response.status_code}): {response.text}")
            return None

    except requests.exceptions.Timeout:
        st.error("⏱️ 요청 타임아웃 (백엔드가 응답하지 않음)")
        return None
    except requests.exceptions.ConnectionError:
        st.error("🔌 백엔드 연결 실패. 백엔드가 실행 중인지 확인하세요.")
        return None
    except Exception as e:
        st.error(f"❌ 오류: {str(e)}")
        return None

def fetch_history(limit: int = 10) -> list:
    """대화 이력 조회"""
    try:
        response = requests.get(
            f"{BACKEND_URL}/history",
            params={"limit": limit},
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("conversations", [])
        else:
            return []

    except:
        return []

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. 사이드바
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

with st.sidebar:
    st.header("⚙️ 설정")

    # 백엔드 상태
    backend_status = check_backend_health()
    if backend_status:
        st.success("✅ 백엔드 연결됨")
    else:
        st.warning("⚠️ 백엔드 연결 실패")

    # API URL 입력 (선택)
    api_url = st.text_input(
        "API URL (기본값: http://localhost:8000)",
        value=BACKEND_URL,
        help="백엔드 API 주소를 변경할 수 있습니다"
    )
    if api_url != BACKEND_URL:
        BACKEND_URL = api_url

    st.divider()

    st.markdown("### 📖 사용 가이드")
    st.markdown("""
    1. 아래 입력창에 질문을 입력하세요
    2. 엔터 또는 버튼을 누르면 GPT가 응답합니다
    3. **대화 이력** 탭에서 과거 질문을 확인할 수 있습니다

    **예시 질문:**
    - "코스피 분석 해줄래?"
    - "AI 트렌드는?"
    - "회의 내용 정리 부탁해"
    """)

    st.divider()
    st.markdown("_AI 3차 세미나 — 사내 GPT 엔터프라이즈 기초 (Step 2)_")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. 메인 콘텐츠 — 두 개 탭
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

tab1, tab2 = st.tabs(["💬 채팅", "📚 대화 이력"])

# ┌─ 탭 1: 채팅
with tab1:
    st.subheader("GPT와 대화하기")

    # 세션 상태 (메시지 히스토리)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 이전 메시지 표시
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 입력 받기
    user_input = st.chat_input("질문을 입력하세요...")

    if user_input:
        # 사용자 메시지 표시
        with st.chat_message("user"):
            st.markdown(user_input)

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # 백엔드 호출 (로딩 표시)
        with st.spinner("🤖 GPT가 생각하는 중..."):
            result = ask_gpt(user_input)

        if result:
            gpt_response = result.get("gpt_response", "응답을 받지 못했습니다.")

            # GPT 메시지 표시
            with st.chat_message("assistant"):
                st.markdown(gpt_response)

            st.session_state.messages.append({
                "role": "assistant",
                "content": gpt_response
            })

            # 성공 메시지
            st.success("✅ 응답 저장 완료!")

# ┌─ 탭 2: 대화 이력
with tab2:
    st.subheader("📚 과거 대화")

    # 이력 조회 버튼
    if st.button("🔄 이력 새로고침", use_container_width=True):
        st.rerun()

    history = fetch_history(limit=20)

    if history:
        st.markdown(f"**총 {len(history)}개의 대화 기록**")

        for idx, conv in enumerate(history, 1):
            with st.expander(f"#{len(history) - idx + 1} — {conv['user_query'][:50]}...", expanded=False):
                st.markdown("**📝 질문:**")
                st.markdown(f"> {conv['user_query']}")

                st.markdown("**💬 답변:**")
                st.markdown(conv['gpt_response'])

                st.markdown(f"_⏰ {conv['timestamp']}_")

    else:
        st.info("아직 대화 이력이 없습니다. 왼쪽 탭에서 질문을 해보세요!")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 6. 푸터
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

st.divider()
st.markdown("""
---
**문제가 발생하면:**
- ✅ 백엔드가 `python main.py`로 실행 중인지 확인
- ✅ 방화벽이 8000포트를 차단하지 않는지 확인
- ✅ API URL이 올바른지 확인 (위 사이드바에서 변경 가능)
""")
