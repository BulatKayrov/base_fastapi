from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000
    prefix: str = '/api'

