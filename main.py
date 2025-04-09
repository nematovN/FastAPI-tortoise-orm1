import asyncio
from db import init_db
from config import get_settings
from tortoise import Tortoise
from fastapi import FastAPI, HTTPException
from schemas.user import BaseUser
from schemas.base import BaseResponse
from models.user import User
from typing import List


settings = get_settings()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="FastApi CRUD Tortoise-orm with aerich",
    debug=settings.app_debug
)



@app.on_event("startup")
async def startup():
    await init_db()
    print("DB Connected ✅")




@app.get("/user/{user_id}", response_model=BaseResponse)
async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "username": user.username
    }
    return BaseResponse(data=data)




# @app.get("/users", response_model=BaseResponse)
# async def get_all_users():
#     users = await User.all()
#     data = [
#         {
#             "id": user.id,
#             "name": user.name,
#             "email": user.email,
#             "username": user.username
#         }
#         for user in users
#     ]
#     return BaseResponse(data={"users": data})






@app.post("/user", response_model=BaseResponse)
async def create_user(user: BaseUser):
    user_data = await User.create(
        name=user.name,
        email=user.email,
        username=user.username
    )

    data = {
        "name": user_data.name,
        "email": user_data.email,
        "username": user_data.username
    }

    return BaseResponse(data=data)



@app.put("/user/{user_id}", response_model=BaseResponse)
async def update_user(user_id: int, user: BaseUser):
    user_data = await User.get_or_none(id=user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    user_data.name = user.name or user_data.name
    user_data.email = user.email or user_data.email
    user_data.username = user.username or user_data.username
    await user_data.save()

    data = {
        "id": user_data.id,
        "name": user_data.name,
        "email": user_data.email,
        "username": user_data.username
    }
    return BaseResponse(data=data)




@app.delete("/user/{user_id}", response_model=BaseResponse)
async def delete_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await user.delete()
    return BaseResponse(data={"id": user_id})
