FROM python:3.13.0a4-slim

ENV PYTHONUNBUFFERED=3.11
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
CMD ["python", "main.py"]
