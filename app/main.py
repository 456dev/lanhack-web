import uvicorn
import os.path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from lanhackbackend.api.data.storage import storage
from lanhackbackend.api.routes.base import api_router
from lanhackfrontend.routes.pages import pages_router

# init fastapi
api = FastAPI()
api.mount(
    "/static",
    StaticFiles(directory=os.path.realpath("./lanhackfrontend/static")),
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
