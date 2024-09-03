from pydantic import BaseModel


class DataBaseConfig(BaseModel):
    HOST: str = 'localhost'
    PORT: int = 5432
    DB: str = 'database'
    USER: str = 'user'
    PASSWORD: str = 'password'
    echo: bool = True
    pool_size: int = 5
    max_overflow: int = 10

