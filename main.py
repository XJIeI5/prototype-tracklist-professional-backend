import flask
from sqlalchemy import exc
from data import db_session
from data import users


app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html")
    
    email, phone = flask.request.form["email"], flask.request.form["phone"]
    sess = db_session.create_session()

    try:
        user = sess.query(users.User).filter(
            (users.User.email == email) & (users.User.phone == int(phone))
        ).one()
    except exc.NoResultFound:
        return "NO USER FOUND"
    return "OK"


def main():
    db_session.global_init("db/data.db")
    app.run(debug=True)


if __name__ == '__main__':
    main()
