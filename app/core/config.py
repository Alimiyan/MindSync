from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MindSync"
    admin_email: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
