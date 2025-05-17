from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
# from backend.models import GameIn, GameOut
# from backend.db import get_games_collection
from api import games
from datetime import date
from pymongo.collection import Collection

app = FastAPI(
    title="Video Games API",
    description="API to add and retrieve video games by release date",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(games.router, prefix="/games", tags=["Games"])


@app.get("/", summary="Health check")
def root():
    return {"message": "Video Games API is running."}
