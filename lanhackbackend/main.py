import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from lanhackbackend.api.data.storage import storage
from lanhackbackend.api.routes.base import api_router
from lanhackfrontend.pages import pages_router

# init fastapi
app = FastAPI()
app.mount("/static", StaticFiles(directory="./lanhackfrontend"), name="static")
app.include_router(api_router, prefix="/api")
app.include_router(pages_router)

# init storage
app.add_event_handler("startup", storage.init)


def main():
    # run server
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
