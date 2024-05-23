from .db_session import SqlAlchemyBase
import sqlalchemy


def parse_stages(stages: str) -> list[str]:
    return stages.split(";")


class Model(SqlAlchemyBase):
    __tablename__ = "models"

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    stages = sqlalchemy.Column(sqlalchemy.String) # NOTE: actually is array
    imageURL = sqlalchemy.Column(sqlalchemy.String)
