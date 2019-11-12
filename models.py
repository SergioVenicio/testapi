import sqlalchemy

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

