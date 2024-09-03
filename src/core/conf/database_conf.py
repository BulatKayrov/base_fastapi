from pydantic import BaseModel


class DataBaseConfig(BaseModel):
    host: str = 'localhost'
    port: int = 5432
    db_name: str = 'database'
    user: str = 'user'
    password: str = 'password'
    echo: bool = True
    pool_size: int = 5
    max_overflow: int = 10

