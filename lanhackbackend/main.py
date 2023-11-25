from fastapi import FastAPI
from lanhackbackend.api.routes import router
import uvicorn

from lanhackbackend.api.data.storage import storage


def main():
    # init fastapi
    app = FastAPI()
    app.include_router(router, prefix="/api")

    # init storage
    storage.init()

    # run server
    uvicorn.run(app, host="localhost", port=8000)

if __name__ == "__main__":
  main()
