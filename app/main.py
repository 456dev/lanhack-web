import uvicorn
import os.path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.data.storage import storage
from backend.routes.api import api_router
from frontend.routes.pages import pages_router

# init fastapi
api = FastAPI()
api.mount(
    "/static",
    StaticFiles(directory=os.path.realpath("./frontend/static")),
    name="static",
)
api.include_router(api_router, prefix="/api")
api.include_router(pages_router)

# init storage
api.add_event_handler("startup", storage.init)


def app():
    # run app on local server
    uvicorn.run(api, host="localhost", port=8000)


if __name__ == "__main__":
    app()
