import database
import models
import schemas


async def create_user(db: database.session, user: schemas.UserCreate):
    new_user = models.User(email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


async def get_users(db: database.session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


async def get_user(db: database.session, user_id: int):
    return db.query(models.User).get(user_id)
