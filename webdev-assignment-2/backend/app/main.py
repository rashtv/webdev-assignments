import uuid
import json

import redis
import uvicorn

from fastapi import FastAPI

app: FastAPI = FastAPI()

r = redis.Redis(
    host="redis",
    port=6379,
    db=0,
    decode_responses=True,
)


@app.get("/api/users/")
async def list_users() -> list:
    users: list = [json.loads(u) for u in r.lrange("users", 0, -1)]
    return users


@app.post("/api/users/")
async def create_user(
    name: str,
) -> dict:
    user: dict = {
        "id": str(uuid.uuid4()),
        "name": name,
    }
    r.rpush(
        "users",
        json.dumps(user),
    )
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
