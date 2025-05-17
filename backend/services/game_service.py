from models.game import GameCreate, GameInDB
from db.session import get_db
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
import datetime


class GameService:
    def __init__(self):
        self.collection: AsyncIOMotorCollection = get_db()["games"]

    async def add_game(self, game: GameCreate) -> GameInDB:
        game_dict = game.dict()
        # Convert release_date to datetime.datetime if it's a date
        if isinstance(game_dict.get("release_date"), datetime.date) and not isinstance(game_dict["release_date"], datetime.datetime):
            game_dict["release_date"] = datetime.datetime.combine(
                game_dict["release_date"], datetime.time())
        result = await self.collection.insert_one(game_dict)
        game_dict["_id"] = str(result.inserted_id)
        return GameInDB(**game_dict)

    async def get_game_by_birthday(self, birthday) -> GameInDB | None:
        # Convert birthday (date) to datetime for MongoDB query
        if isinstance(birthday, datetime.date) and not isinstance(birthday, datetime.datetime):
            birthday_dt = datetime.datetime.combine(birthday, datetime.time())
        else:
            birthday_dt = birthday
        game = await self.collection.find_one({"release_date": birthday_dt})
        if game:
            game["_id"] = str(game["_id"])
            return GameInDB(**game)
        return None
