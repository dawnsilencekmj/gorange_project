from fastapi import APIRouter, Query
from app.services.stock_service import StockService

router = APIRouter()
service = StockService()


@router.get("/rows")
def rows(limit: int = 100, symbols: list[str] = Query(default=[])):
    return service.get_rows(limit=limit, symbols=symbols)
