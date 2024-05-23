import datetime 
import flask
from flask import jsonify, make_response, request
from data.orders import Order
from data.users import User
from data.models import Model, parse_stages as ps

from . import db_session


orders_blueprint = flask.Blueprint(
    'order_api',
    __name__,
    template_folder='templates'
)

def password_ok(password: str) -> bool:
    return True


def parse_stages(stages: str) -> dict:
    parsed_stages = {}
    for i in stages.split(';'):
        parsed_stages[int(i.split(':')[0])] = int(i.split(':')[1])
    return parsed_stages


def make_stages(parsed_stages: dict) -> str:
    a = [f'{i}:{parsed_stages[i]}' for i in parsed_stages]
    return ','.join(a)


def init_stages(modelId: int, amount: int) -> str:
    sess = db_session.create_session()
    stages_name = sess.query(Model).filter(
        (Model.id == modelId)
    ).first()

    stages_amount = {}
    stages_amount[1] = amount
    for i in range(1, len(ps(stages_name.stages))):
        stages_amount[i+1] = 0

    res = ""
    for key, value in stages_amount.items():
        res += f"{key}:{value};"
    return res[:-1]


@orders_blueprint.route('/api/reg_order', methods=['POST'])
def register_order():
    db_sess = db_session.create_session()
    password = request.json["password"]
    if password_ok(password):
        order = Order(
            modelId=request.json['modelId'],
            userId=request.json["userId"],
            amount=request.json["amount"],
            dataCreate=datetime.datetime.today(),
            dataExpected=datetime.datetime.strptime(request.json["dataExpected"], "%Y-%m-%d").date(),
            paid=request.json["paid"],
            stages=init_stages(request.json['modelId'], request.json["amount"])
        )
        db_sess.add(order)
        db_sess.commit()
        return jsonify({"succes": f"order id: {order.id}"})
    else:
        return jsonify({"error": 'Incorrect Password'})


@orders_blueprint.route("/api/upd_order", methods=['PUT'])
def update_order(order_id):
    order_id = request.json['order_id']
    try:
        order_id = int(order_id)
    except ValueError:
        return make_response(jsonify({'error': 'Bad Request'}), 400)

    if not request.json:
        return make_response(jsonify({"error": 'Bad Request'}), 400)

    db_sess = db_session.create_session()
    order = db_sess.query(Order).get(order_id)

    if not order:
        return make_response(jsonify({'error': 'Not found'}), 404)
    data = request.json()
    user = db_sess.query(User).filter(User.id == data['stage_id'])

    parsed_stages = parse_stages(order.stages)
    parsed_stages[data['stage_id']] -= 1
    if data["state"] == 'OK':
        parsed_stages[data['stage_id'] + 1] += 1
    else:
        parsed_stages[1] += 1
    stages = make_stages(parsed_stages)
    order.stages = stages
    db_sess.commit()

    return jsonify({'success': 'OK'})




