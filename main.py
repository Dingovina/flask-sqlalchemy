from data import db_session
from data.users import User
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from data import db_session


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Join')


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    # app.run()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template('login.html', title='Авторизация', form=form)
    elif request.method == 'POST':
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        flag = True
        try:
            login = request.form['login']
            password = request.form['password']
            repeat_password = request.form['repeat_password']
            surname = request.form['surname']
            name = request.form['name']
            age = int(request.form['age'])
            position = request.form['position']
            speciality = request.form['speciality']
            address = request.form['address']
            print(login, password, surname, name, age, position, speciality, address, sep='\n')
        except Exception:
            return "Поля заполнены неверно"
        if flag:
            if password == repeat_password:
                user = User()
                user.email = login
                user.hashed_password = password
                user.surname = surname
                user.name = name
                user.age = age
                user.position = position
                user.speciality = speciality
                user.address = address
                db_sess.add(user)
                db_sess.commit()
                return "Форма отправлена"
            else:
                return "Пароли различаются"


if __name__ == '__main__':
    main()
    app.run(port=5000, host='127.0.0.1')
