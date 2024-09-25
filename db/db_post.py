from datetime import datetime
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost


def create(db: Session, request: PostBase):
  new_post = DbPost(
    caption = request.caption,
    mediasourcs = request.mediasourcs,
    date_time_create = datetime.datetime.now(),
    user_id = request.user_id
  )
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post