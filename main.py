from fastapi import FastAPI

from src.Route import Routes

def get_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(Routes().get_routes())

    url_list = [{'path': route.path, 'name': route.name} for route in app.routes]

    print(url_list)
    return app
