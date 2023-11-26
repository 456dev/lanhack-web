from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates

pages_router = APIRouter()
templates = Jinja2Templates(directory="./frontend/templates")


# serve index.html
@pages_router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
