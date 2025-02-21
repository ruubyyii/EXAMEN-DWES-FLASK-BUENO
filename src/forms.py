from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import EqualTo, Email, ValidationError, Length, DataRequired

class RegisterForm(FlaskForm):

    email = EmailField('Email:', validators=[
        DataRequired(),
        Length(min=3, max=50),
        Email()
    ])

    password = PasswordField('Password:', validators=[
        DataRequired(),
        Length(min=3, max=50),
        EqualTo('confirm', message='Las contraseñas no coinciden.')
    ])

    confirm = PasswordField('Repeat password:', validators=[
        DataRequired(),
        Length(min=3, max=50)
    ])

    fullname = StringField('Nombre completo:', validators=[
        DataRequired(),
        Length(min=1, max=50)
    ])

    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):

    email = EmailField('Email:', validators=[
        DataRequired(),
        Length(min=3, max=50),
        Email()
    ])

    password = PasswordField('Password:', validators=[
        DataRequired(),
        Length(min=3, max=50)
    ])

    submit = SubmitField('Iniciar sesion')

class ContactForm(FlaskForm):

    fullname = StringField('Nombre completo:', validators=[
        DataRequired(),
        Length(min=1, max=50)
    ])

    number = StringField('Numero:', validators=[
        DataRequired(),
        Length(min=9, max=9)
    ])

    email = EmailField('Email:', validators=[
        DataRequired(),
        Length(min=3, max=50)
    ])

    submit = SubmitField('Iniciar sesion')