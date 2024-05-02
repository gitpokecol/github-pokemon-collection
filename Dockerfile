FROM python:3.10
WORKDIR /app

# 소스 추가
COPY src /app/src
COPY templates /app/templates
COPY requirements.txt /app/requirements.txt
COPY static /app/static

# 앱 의존성
RUN pip install -r requirements.txt

# 실행
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
