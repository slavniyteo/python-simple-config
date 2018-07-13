import os
from typing import Dict

from .config import Config


class ConfigLoader(object):
    __instance = None

    @staticmethod
    def instance(prefix: str):
        if not ConfigLoader.__instance:
            ConfigLoader.__instance = ConfigLoader(prefix)
        return ConfigLoader.__instance

    @staticmethod
    def _load_config(prefix) -> Config:
        envs: Dict[str, str] = os.environ
        config_vars = {}
        for key, value in envs.items():
            if key.startswith(prefix):
                config_vars[key[len(prefix):].lower()] = value

        return Config(config_vars)

    def __init__(self, prefix: str):
        self.__config = self._load_config(prefix)

    @property
    def config(self) -> Config:
        return self.__config
