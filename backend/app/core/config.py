from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ai_assessment_platform"
    app_version: str = "0.1.0"
    app_env: str = "development"

    api_host: str = "127.0.0.1"
    api_port: int = 8000

    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "ai_assessment_platform"

    groq_api_key: str = ""

    streamlit_api_url: str = "http://127.0.0.1:8000"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()