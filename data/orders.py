from .db_session import SqlAlchemyBase
import sqlalchemy


class Order(SqlAlchemyBase):
    __tablename__ = "orders"

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    modelId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("models.id"))
    userId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    amount = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self) -> str:
        return f"<Order> {self.id}"
