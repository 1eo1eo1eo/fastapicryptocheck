from fastapi import APIRouter

from core.config import settings

from .init import cmc_client


router = APIRouter(
    prefix=settings.api.currencies_prefix,
)

@router.get("")
async def get_cryptocurrency():
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrencies(currency_id: int):
    return await cmc_client.get_currency(currency_id)