from dotenv import load_dotenv
from typing import TypedDict
from os import getenv

load_dotenv()

class ConfigType(TypedDict):
    MODEL_CACHE_DIR: str | None
    TEXT_GENERATION_MODEL: str
    TEXT_GENERATION_MAXIMUM_RESULTS: int
    CONVERSATION_GENERATION_MODEL: str
    DISCORD_BOT_TOKEN: str
    DISCORD_DEBUG_GUILDS: list[int] | None

def get_debug_guilds() -> list[int] | None:
    debug_guilds = getenv("DISCORD_DEBUG_GUILDS")
    if debug_guilds:
        return [ int(e) for e in (debug_guilds.split(",")) ]
    return None

config: ConfigType = {
    "MODEL_CACHE_DIR": getenv("MODEL_CACHE_DIR", default='') or None,
    "TEXT_GENERATION_MODEL": getenv("TEXT_GENERATION_MODEL", default="distilgpt2"),
    "TEXT_GENERATION_MAXIMUM_RESULTS": int(getenv("TEXT_GENERATION_MAXIMUM_RESULTS", default=3)),
    "CONVERSATION_GENERATION_MODEL": getenv("CONVERSATION_GENERATION_MODEL", default="deepparag/Aeona"),
    "DISCORD_BOT_TOKEN": getenv("DISCORD_BOT_TOKEN"),
    "DISCORD_DEBUG_GUILDS": get_debug_guilds()
}
