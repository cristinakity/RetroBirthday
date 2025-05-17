from fastapi import APIRouter, HTTPException
from datetime import date
from models.game import GameCreate, GameInDB
from services.game_service import GameService

router = APIRouter()

game_service = GameService()


@router.post("", response_model=GameInDB)
async def add_game(game: GameCreate):
    return await game_service.add_game(game)

# /game?date=${this.birthdate}


@router.get("", response_model=GameInDB)
async def get_game_by_birthday(date: date):
    game = await game_service.get_game_by_birthday(date)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
