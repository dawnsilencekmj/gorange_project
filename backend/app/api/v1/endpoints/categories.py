from fastapi import APIRouter
from app.services.stock_service import StockService

router = APIRouter()
service = StockService()


@router.get("/stats")
def category_stats():
    return service.get_category_stats()
