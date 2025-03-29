from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    """Application settings."""
    
    # Bot settings
    BOT_TOKEN: SecretStr
    
    # Logging settings
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create global settings instance
settings = Settings() 