from fastapi import APIRouter
from app.services.stock_service import StockService

router = APIRouter()
service = StockService()


@router.get('/rule-demo')
def rule_demo(vol_threshold: float = 0.02):
    return service.rule_demo(vol_threshold=vol_threshold)
