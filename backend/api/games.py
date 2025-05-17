from fastapi import APIRouter, HTTPException
from datetime import date
from models.game import GameCreate, GameInDB
from services.game_service import GameService

router = APIRouter()

game_service = GameService()


@router.post("/", response_model=GameInDB)
async def add_game(game: GameCreate):
    return await game_service.add_game(game)


@router.get("/by-birthday/{birthday}", response_model=GameInDB)
async def get_game_by_birthday(birthday: date):
    game = await game_service.get_game_by_birthday(birthday)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


# from fastapi import APIRouter, HTTPException, Depends
# from backend.models import GameIn, GameOut
# from backend.db import get_games_collection
# from datetime import date
# from pymongo.collection import Collection

# router = APIRouter(
#     prefix="/games",
#     tags=["games"]
# )


# @router.post("/", response_model=GameOut, summary="Add a new video game")
# def add_game(game: GameIn, games_collection: Collection = Depends(get_games_collection)):
#     game_dict = game.dict()
#     result = games_collection.insert_one(game_dict)
#     game_dict["id"] = str(result.inserted_id)
#     return GameOut(**game_dict)


# @router.get("/by-birthday/{birthday}", response_model=GameOut, summary="Get a game released on your birthday")
# def get_game_by_birthday(birthday: date, games_collection: Collection = Depends(get_games_collection)):
#     game = games_collection.find_one({"release_date": birthday.isoformat()})
#     if not game:
#         raise HTTPException(
#             status_code=404, detail="No game found for this date")
#     game["id"] = str(game["_id"])
#     return GameOut(**game)
