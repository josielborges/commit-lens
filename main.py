import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.git_commits_evaluation_endpoints import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router, prefix='/commits')


@app.get("/")
def get_app_status() -> dict[str, str]:
    return {
        'status': 'ok',
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
