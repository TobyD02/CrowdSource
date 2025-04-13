from typing_extensions import Self
from typing import List
from configparser import ConfigParser
import os


class ConfigProvider:
    def __init__(self: Self):
        self.config_parser: ConfigParser = ConfigParser()

        self.config_parser.read(
           os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "..", "config.ini"
                )
            )
        )

    def get_config(self: Self) -> ConfigParser:
        return self.config_parser
