import flask
import json
from sqlalchemy import exc
from data import db_session
from data import users, orders, order_api, models
from mock import calls_test
from datetime import date


def jsonify_user_orders(user_orders: list[orders.Order]) -> list[dict]:
    res = []
    for order in user_orders:
        res.append(order.dict())
    return res


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html", calls=[], email=None)
    
    email, phone, name = flask.request.form["email"], int(flask.request.form["phone"]), flask.request.form["name"]
    sess = db_session.create_session()

    try:
        user = sess.query(users.User).filter(
            (users.User.email == email) & (users.User.phone == phone) & (users.User.name == name)
        ).one()
        users_orders = sess.query(orders.Order).filter(
            (orders.Order.userId == user.id) 
        ).all()
        nameStages = []
        for order in users_orders:
            name_stages = sess.query(models.Model).filter(
                (models.Model.id == order.modelId)
            ).first()
            nameStages.append(models.parse_stages(name_stages.stages))
        return flask.render_template("login.html",
                                     calls=jsonify_user_orders(user_orders=users_orders),
                                     nameStages=nameStages,
                                     name=name,
                                     phone=phone,
                                     email=email)
    except exc.NoResultFound:
        return "NO USER FOUND"
    return "OK"


def main():
    db_session.global_init("db/data.db")
    app.register_blueprint(order_api.orders_blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()
