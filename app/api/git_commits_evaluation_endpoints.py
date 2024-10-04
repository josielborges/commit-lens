from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(tags=['Improvements'])
templates = Jinja2Templates(directory="app/templates")


@router.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("git_commits_evaluation_form.html", {"request": request})
