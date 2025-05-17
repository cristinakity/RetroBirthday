# Video Games FastAPI Backend

## Features

- Add video games with title, release date, and description.
- Retrieve a video game released on a specific date (e.g., your birthday).
- MongoDB for persistent storage.
- Automatic Swagger docs at `/docs`.

## Setup

1. Install dependencies:

   ```
   pip3 install -r requirements.txt
   ```

2. Start the server:

   ```
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Open the API docs:
   ```
   $BROWSER http://localhost:8000/docs
   ```

## Endpoints

- `POST /games/` — Add a new video game.
- `GET /games/by-birthday/{birthday}` — Get a game released on a specific date.
