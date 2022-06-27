FROM python:alpine

WORKDIR /app

COPY requirements.txt ./
RUN apk add -U --no-cache build-base libffi-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base

ENV MODEL_CACHE_DIR="/cache" \
    TEXT_GENERATION_MODEL="distilgpt2" \
    TEXT_GENERATION_MAXIMUM_RESULTS=3 \
    CONVERSATION_GENERATION_MODEL="deepparag/Aeona" \
    DISCORD_BOT_TOKEN="" \
    DISCORD_DEBUG_GUILDS=""

COPY . .

CMD [ "python", "./src/main.py" ]
