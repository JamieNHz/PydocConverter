FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgdiplus \
    fonts-dejavu \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY convert.py .

ENTRYPOINT ["python", "/app/convert.py"]
