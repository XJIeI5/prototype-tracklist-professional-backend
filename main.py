import flask
from data import db_session


app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"


def main():
    db_session.global_init("db/data.db")
    app.run()


if __name__ == '__main__':
    main()
