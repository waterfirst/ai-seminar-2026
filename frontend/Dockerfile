FROM python:3.11-slim

WORKDIR /app

# Streamlit 포트 설정
EXPOSE 8501

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY app.py .

# Streamlit 캐시 디렉토리 설정
RUN mkdir -p ~/.streamlit && \
    echo "[client]\n\
showErrorDetails = false\n\
[server]\n\
port = 8501\n\
headless = true\n\
" > ~/.streamlit/config.toml

# 실행
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
