FROM python:3.9-slim

WORKDIR /app

COPY gauge1.py .

RUN pip install prometheus_client

EXPOSE 8000
EXPOSE 8001

CMD ["python", "gauge1.py"]