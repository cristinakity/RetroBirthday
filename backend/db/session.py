
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)


def get_db():
    return client[settings.DB_NAME]
