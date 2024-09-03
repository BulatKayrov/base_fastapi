import pathlib

from pydantic_settings import BaseSettings

from .database_conf import DataBaseConfig
from .run_config import RunConfig

BASE_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBaseConfig = DataBaseConfig()

    @property
    def url(self):
        if self.run.debug:
            return f'sqlite+aiosqlite://{BASE_DIR}/database.db'
        return f'postgresql+asyncpg://{self.db.USER}:{self.db.PASSWORD}@{self.db.HOST}:{self.db.PORT}/{self.db.DB}'
