import sqlalchemy
from sqlalchemy import String, BIGINT, DATETIME, Column

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def _as_dict():
    val = {
        'user_id': User.user_id,
        'name': User.name,
        'email': User.email
    }
    return val


class User(Base):
    __tablename__ = "user_table"
    user_id = Column(BIGINT, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String, nullable=False)
