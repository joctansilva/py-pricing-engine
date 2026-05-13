import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    MONGO_URL: str = os.getenv("MONGO_URL", "")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "pricing_logs")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CELERY_BROKER: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/1")
    CELERY_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/2")
    CACHE_TTL: int = int(os.getenv("CACHE_TTL_SECONDS", "3600"))
    QUOTATION_VALIDITY_DAYS: int = 30
    MAX_SIMULATION_SCENARIOS: int = 5


settings = Settings()
