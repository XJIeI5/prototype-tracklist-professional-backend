from .db_session import SqlAlchemyBase
import sqlalchemy


class Model(SqlAlchemyBase):
    __tablename__ = "models"

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    # actually is array
    stages = sqlalchemy.Column(sqlalchemy.String) 
