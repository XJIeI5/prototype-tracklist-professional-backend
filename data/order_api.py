import flask
from flask import jsonify, make_response, request
from data.orders import Order
from data.users import User

from . import db_session


orders_blueprint = flask.Blueprint(
    'order_api',
    __name__,
    template_folder='templates'
)


def parse_stages(stages: str) -> dict:
    parsed_stages = {}
    for i in stages.split(','):
        parsed_stages[int(i.split(':')[0])] = int(i.split(':')[1])
    return parsed_stages


def make_stages(parsed_stages: dict) -> str:
    a = [f'{i}:{parsed_stages[i]}' for i in parsed_stages]
    return ','.join(a)


@orders_blueprint.route('/api/reg_order', methods=['POST'])
def register_order(order_id):
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
    return None #   to do: order creation


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




