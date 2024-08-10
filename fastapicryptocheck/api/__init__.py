from fastapi import APIRouter

from core.config import settings
from .get_crypto_currencies import router as get_crypto_currencies_router


router = APIRouter(
    prefix=settings.api.prefix
)