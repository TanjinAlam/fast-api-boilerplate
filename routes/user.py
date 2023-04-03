from datetime import datetime
from fastapi import HTTPException
from config.db import session
from decouple import config
from fastapi import APIRouter
from models.index import Users
from schema.index import User
user_router = APIRouter()

@user_router.get("/query_by_user_id/{user_id}")
async def read_user(user_id: int):
    try:
        return session.query(Users).filter(Users.id == user_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="User not found")
    

@user_router.get("/get_all_user")
async def read_user():    
    try:
        res = session.query(Users).all()
    except Exception:
        res = []
    return res


@user_router.post("/regiser_user")
async def write_user(user : User):
    try:
        user_data = Users(
                name = user.name,
                email = user.email,
        )
        session.add(user_data)
        session.commit()
        session.refresh(user_data)
        return session.query(Users).filter_by(id=user_data.id).first()
    except Exception as e:
        print(e) 
        session.rollback()
        return []





