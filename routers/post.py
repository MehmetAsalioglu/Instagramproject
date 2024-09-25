from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from routers.schemas import PostBase, PostDisplay
from fastapi.exceptions import HTTPException
from db import db_post


router = APIRouter(
  prefix='/post',
  tags=['post']
)


@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
           return db_post.create(db, request)