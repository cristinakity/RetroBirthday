from models.game import GameCreate, GameInDB
from db.session import get_db
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId


class GameService:
    def __init__(self):
        self.collection: AsyncIOMotorCollection = get_db()["games"]

    async def add_game(self, game: GameCreate) -> GameInDB:
        game_dict = game.dict()
        result = await self.collection.insert_one(game_dict)
        game_dict["_id"] = str(result.inserted_id)
        return GameInDB(**game_dict)

    async def get_game_by_birthday(self, birthday) -> GameInDB | None:
        game = await self.collection.find_one({"release_date": birthday})
        if game:
            game["_id"] = str(game["_id"])
            return GameInDB(**game)
        return None
