import uvicorn
from fastapi import FastAPI

from lanhackbackend.api.data.storage import storage
from lanhackbackend.api.routes.base import api_router

# init fastapi
app = FastAPI()
app.include_router(api_router, prefix="/api")

# init storage
storage.init()

def main():
    # run server
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
