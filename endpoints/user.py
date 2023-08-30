from fastapi import APIRouter
from sqlalchemy import and_
from db.db import Database
from models.model import User, Base
from models.response import Response

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "404 Not Found"}},
)

database = Database()
engine = database.get_db_connection()
# Base.metadata.create_all(engine)

@router.get("/222")
async def create_user():
    session = database.get_db_session(engine)
    obj = User(name="deancoco", age=18)
    session.add(obj)
    session.commit()
    return Response({}, 200, 'User create success', False)


@router.get("/")
async def read_all_users():
    session = database.get_db_session(engine)
    data = session.query(User).all()
    return Response(data, 200, "All User retrieved successfully.", False)


@router.get('/{user_id}')
async def get_user(user_id: int):
    session = database.get_db_session(engine)
    response_message = "User retrieved successfully"
    data = None
    try:
        data = session.query(User).filter(
            and_(User.id == user_id)).one()
    except Exception as ex:
        print("Error:", ex)
        response_message = "User Not found"
    error = False

    return Response(data, 200, response_message, error)
