from typing import Any, Dict

from .singleton import Singleton


class ConfigBase(Dict[str, Any], Singleton):
    LOG_LEVEL: str = "debug"
    MODE: str = "dev"
