from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from core.config import settings
from api import router as api_router

main_app = FastAPI()

main_app.include_router(
    api_router,
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://172.29.0.2:5173",
]

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
)