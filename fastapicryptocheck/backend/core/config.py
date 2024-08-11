from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class APIPrefix(BaseModel):
    prefix: str = "/api"
    currencies_prefix: str = "/cryptocurrencies"

class Settings(BaseSettings):
    CMC_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
    )

    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()


settings = Settings() #type: ignore