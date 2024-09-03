from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import router
from core.conf import settings
from core.models import helper

@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    yield
    await helper.dispose()


_app = FastAPI()
_app.include_router(router=router, prefix=settings.run.prefix)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:_app", host=settings.run.host, port=settings.run.port, reload=True)