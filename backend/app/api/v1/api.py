from fastapi import APIRouter
from app.api.v1.endpoints import dashboard, categories, explorer, playground

api_router = APIRouter()
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(explorer.router, prefix="/explorer", tags=["explorer"])
api_router.include_router(playground.router, prefix="/playground", tags=["playground"])
