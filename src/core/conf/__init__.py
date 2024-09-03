__all__ = ['settings']

from .settings import Settings

settings = Settings(_env_file='.env')
