from fastapi import APIRouter, Query
from app.services.stock_service import StockService

router = APIRouter()
service = StockService()


@router.get("/kpi")
def get_kpi(date_from: str | None = None, date_to: str | None = None):
    return service.get_kpi(date_from=date_from, date_to=date_to)


@router.get("/timeseries")
def get_timeseries(symbols: list[str] = Query(default=[]), date_from: str | None = None, date_to: str | None = None):
    return service.get_timeseries(symbols=symbols, date_from=date_from, date_to=date_to)
