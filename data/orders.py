from .db_session import SqlAlchemyBase
import sqlalchemy
import datetime


def parse_stages(stages: str) -> dict:
    res = {}
    for stage in stages.split(";"):
        s = stage.split(":")
        stage_name, amount_on_stage = int(s[0]), int(s[1])
        res[stage_name] = amount_on_stage
    return res


class Order(SqlAlchemyBase):
    __tablename__ = "orders"

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    modelId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("models.id"))
    userId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    amount = sqlalchemy.Column(sqlalchemy.Integer)
    dataCreate = sqlalchemy.Column(sqlalchemy.Date)
    dataExpected = sqlalchemy.Column(sqlalchemy.Date)
    paid = sqlalchemy.Column(sqlalchemy.Boolean)
    stages = sqlalchemy.Column(sqlalchemy.String) # NOTE: actually is a dict with stage and amount of detail on curr stage
                                                  # fetches stage names from models and initiate it with zeroes

    def __repr__(self) -> str:
        return f"<Order> {self.id}"

    def dict(self) -> dict:
        return {
            "id": self.id,
            "modelId": self.modelId,
            "userId":self.userId,
            "productTotals": self.amount,
            "dateCreate": datetime.datetime.strftime(self.dataCreate, "%d.%m.%y"),
            "dateExpected": datetime.datetime.strftime(self.dataExpected, "%d.%m.%y"),
            "paid": self.paid,
            "stages": parse_stages(self.stages)
        }    
