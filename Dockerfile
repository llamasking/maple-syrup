FROM python:slim

WORKDIR /app

COPY requirements.txt ./
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential cmake cmake-extras git && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential cmake cmake-extras git --auto-remove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV MODEL_CACHE_DIR="/cache" \
    TEXT_GENERATION_MODEL="distilgpt2" \
    TEXT_GENERATION_MAXIMUM_RESULTS=3 \
    CONVERSATION_GENERATION_MODEL="deepparag/Aeona" \
    DISCORD_BOT_TOKEN=""

COPY . .

CMD [ "python", "./src/main.py" ]
