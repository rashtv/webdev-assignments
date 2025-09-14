import uuid
import random

import uvicorn

from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/api/users/")
async def get_users() -> list:
    users: list = [
        {
            "id": i,
            "name": uuid.uuid4(),
        } for i in range(
            random.randint(
                a=1,
                b=10,
            ),
        )
    ]
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
