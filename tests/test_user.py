if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = ""

from data import db_session
from data import users
import sqlalchemy as sqla
from sqlalchemy.orm import Session
import unittest

test_db = "db/test.db"

class DummyUser:
    email = "123@mail.org"
    phone = 79158151712

    @staticmethod
    def get(email: str = "", phone: int = 0) -> users.User:
        user = users.User()
        user.email = DummyUser.email if not email else email
        user.phone = DummyUser.phone if not phone else phone
        return user


def clear_db(sess: Session) -> None:
    for table in reversed(db_session.SqlAlchemyBase.metadata.sorted_tables):
        sess.execute(table.delete())
    sess.commit()

class TestUser(unittest.TestCase):
    def test_get(self) -> None:
        sess = db_session.create_session()
        sess.add(DummyUser.get(email="abc@ya.ru"))
        sess.add(DummyUser.get())
        sess.commit()

        user = sess.query(users.User).filter(
            users.User.id == 2
        ).one()
        self.assertEqual(user.email, DummyUser.email, "wrong email")
        self.assertEqual(user.phone, DummyUser.phone, "wrong phone")
        clear_db(sess)

    
if __name__ == "__main__":
    db_session.global_init(test_db)
    unittest.main()
