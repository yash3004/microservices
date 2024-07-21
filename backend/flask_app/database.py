import sqlalchemy
from sqlalchemy import String, BIGINT, DATETIME, Column


class User:
    Created_at = Column(DATETIME)
