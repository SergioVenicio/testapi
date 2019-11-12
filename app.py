import sqlalchemy
from fastapi import FastAPI, Depends, HTTPException

from typing import List

import database
import models
import schemas
import crud



database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(__name__)


@app.post('/user', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: database.session = Depends(database.get_db)):
    try:
        db_user = crud.create_user(db, user)
        return await db_user
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail='Email already exists!')


@app.get('/users/', response_model=List[schemas.User])
async def get_users(skip: int = 0, limit: int = 100, db: database.session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return await users


@app.get('/users/{user_id}', response_model=schemas.User)
async def get_user(user_id: int, db: database.session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail='User not found!')

    return await db_user
