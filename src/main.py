from fastapi import FastAPI

from api import router
from core.conf import settings

app = FastAPI()
app.include_router(router=router, prefix=settings.run.prefix)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host=settings.run.host, port=settings.run.port, reload=True)