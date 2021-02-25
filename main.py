from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'John'
    user.name = 'Rain'
    user.age = 32
    user.position = 'lowest'
    user.speciality = 'sleeper'
    user.address = 'module_2'
    user.email = 'john_rain@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Andy'
    user.name = 'Ydna'
    user.age = 22
    user.position = 'cap helper'
    user.speciality = 'space scientist'
    user.address = 'module_1'
    user.email = 'best_andy123@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Karl'
    user.name = 'Ltak'
    user.age = 19
    user.position = 'lowest'
    user.speciality = 'ship cleaner'
    user.address = 'module_9'
    user.email = 'ilovemywork@mars.org'
    db_sess.add(user)
    db_sess.commit()


    #app.run()


if __name__ == '__main__':
    main()