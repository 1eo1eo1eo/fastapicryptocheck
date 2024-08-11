from fastapi import APIRouter

from core.config import settings
from api_import.http_client import CMCHTTPClient


router = APIRouter(
    prefix=settings.api.prefix,
    tags=["CryptoCurrencies"],
)

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY,
)

@router.get("/cryptocurrencies")
async def get_cryptocurrency():
    return await cmc_client.get_listings()


@router.get("/cryptocurrencies/{currency_id}")
async def get_cryptocurrencies(currency_id: int):
    return await cmc_client.get_currency(currency_id)