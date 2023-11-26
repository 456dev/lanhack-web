import os.path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.data.storage import storage
from backend.routes.api import api_router
from frontend.routes.pages import pages_router

# init fastapi
app = FastAPI()

# locate static files for frontend
app.mount(
    "/static",
    StaticFiles(directory=os.path.realpath("./frontend/static")),
    name="static",
)

# link routes for frontend and backend
app.include_router(api_router, prefix="/api")
app.include_router(pages_router)

# init storage
app.add_event_handler("startup", storage.init)


def main():
    # run app on local server
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
