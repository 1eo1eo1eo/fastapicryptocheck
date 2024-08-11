from fastapi import APIRouter

from core.config import settings
from api_import.http_client import CMCHTTPClient
from .get_crypto_currencies import router as get_crypto_currencies_router


router = APIRouter(
    prefix=settings.api.prefix
)

router.include_router(
    get_crypto_currencies_router,
)