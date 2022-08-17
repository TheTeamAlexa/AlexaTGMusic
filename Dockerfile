FROM python:3.8.3-alpine
RUN pip install --upgrade pip
FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
