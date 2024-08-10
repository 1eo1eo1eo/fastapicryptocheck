from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class APIPrefix(BaseModel):
    prefix: str = "/api"

class Settings(BaseSettings):
    #CMC_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_prefix="CMC__",
    )

    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()


settings = Settings()