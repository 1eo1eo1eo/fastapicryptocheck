from fastapi import APIRouter

from core.config import settings


router = APIRouter(
    prefix=settings.api.prefix,
    tags=["CryptoCurrencies"]
)

@router.get("/cryptocurrencies/{currency_id}")
def get_cryptocurrency(currency_id: int):
    pass