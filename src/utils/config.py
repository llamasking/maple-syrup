from dotenv import load_dotenv
from typing import TypedDict
from os import getenv


# Read config
load_dotenv()

class ConfigType(TypedDict):
    TEXT_GENERATION_MODEL: str
    TEXT_GENERATION_MAXIMUM_RESULTS: int
    CONVERSATION_GENERATION_MODEL: str
    DISCORD_BOT_TOKEN: str
    DISCORD_DEBUG_GUILDS: list[int]

config: ConfigType = {
    "TEXT_GENERATION_MODEL": getenv("TEXT_GENERATION_MODEL", default="distilgpt2"),
    "TEXT_GENERATION_MAXIMUM_RESULTS": int(getenv("TEXT_GENERATION_MAXIMUM_RESULTS", default=3)),
    "CONVERSATION_GENERATION_MODEL": getenv("CONVERSATION_GENERATION_MODEL", default="deepparag/Aeona"),
    "DISCORD_BOT_TOKEN": getenv("DISCORD_BOT_TOKEN"),
    "DISCORD_DEBUG_GUILDS": [ int(element) for element in getenv("DISCORD_DEBUG_GUILDS").split(",") ]
}
