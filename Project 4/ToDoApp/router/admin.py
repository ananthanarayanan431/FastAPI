

from fastapi import FastAPI, APIRouter, HTTPException, Path
from models import Todos, Users
from starlette import status
from database import SessionLocal
from .auth import get_current_user
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/admin",
    tags=['admin']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):

    if user is None or user.get('user_role').lower() != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed!")
    
    return db.query(Todos).all()

@router.delete("/todo",status_code=status.HTTP_200_OK)
async def delete_todo(user: user_dependency, db: db_dependency, todo_int:int = Path(gt=0)):

    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failes")
    
    todo_model = db.query(Todos).filter(Todos.id==todo_int).first()

    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    
    db.query(Todos).filter(Todos.id==todo_int).delete()
    db.commit()