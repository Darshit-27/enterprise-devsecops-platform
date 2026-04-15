FROM python:3.9-slim

WORKDIR /app

COPY app/ /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "app.py"]
