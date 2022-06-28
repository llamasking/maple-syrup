FROM python:slim

WORKDIR /app

COPY requirements.txt ./
#RUN pip install --no-cache-dir transformers transformers[torch] && \
#    pip install --no-cache-dir --pre py-cord py-cord[speed] && \
#    pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_CACHE_DIR="/cache" \
    TEXT_GENERATION_MODEL="distilgpt2" \
    TEXT_GENERATION_MAXIMUM_RESULTS=3 \
    CONVERSATION_GENERATION_MODEL="deepparag/Aeona" \
    DISCORD_BOT_TOKEN="" \
    DISCORD_DEBUG_GUILDS=""

COPY . .

CMD [ "python", "./src/main.py" ]
