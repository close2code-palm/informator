import configparser
from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Telegram:
    """Telegram data"""
    bot_token: str


@dataclass(frozen=True)
class Database:
    """Database settings"""

    host: str
    driver: str
    user: str
    password: str
    database: str
    port: Optional[int]

    @property
    def db_url(self) -> str:
        port = f':{self.port}' if self.port else ''
        return f'{self.driver}://{self.user}:{self.password}' \
               f'@{self.host}{port}/{self.database}'


@dataclass(frozen=True)
class Config:
    """Composed config data"""
    telegram: Telegram
    database: Database


def read_config(config_file_path) -> Config:
    """Reads config in entry point
    Used once"""
    config = configparser.ConfigParser()
    config.read(config_file_path)

    telegram = config['telegram']
    database = config['database']

    database_params = Database(
        database.get('host'),
        database.get('driver'),
        database.get('user'),
        database.get('password'),
        database.get('database'),
        database.get('port'),
    )
    return Config(Telegram(telegram.get('BOT_TOKEN')),
                  database_params)
