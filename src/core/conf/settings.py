from pydantic_settings import BaseSettings

from .run_config import RunConfig


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
