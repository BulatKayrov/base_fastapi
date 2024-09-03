import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict

from .database_conf import DataBaseConfig
from .run_config import RunConfig

BASE_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix='APP_CONFIG__',
        env_nested_delimiter='__'
    )
    base_dir: pathlib.Path = BASE_DIR
    run: RunConfig = RunConfig()
    db: DataBaseConfig = DataBaseConfig()

    @property
    def url(self):
        if self.run.debug:
            return f'sqlite+aiosqlite:///{self.db.db_name}.sqlite3'
        return f'postgresql+asyncpg://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.db_name}'
