import uvicorn
from fastapi import FastAPI

from lanhackbackend.api.data.storage import storage
from lanhackbackend.api.routes.base import api_router


def main():
    # init fastapi
    app = FastAPI()
    app.include_router(api_router, prefix="/api")

    # init storage
    storage.init()

    # run server
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
