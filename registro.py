from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class CadastraUsuarioForm(FlaskForm):
    username = StringField('Usuário',validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    senha = PasswordField('Digite a senha',validators=[DataRequired(), Length(min=8, max=80)])
    repita_senha = PasswordField('Repita a senha',validators=[DataRequired(), EqualTo('repita_senha', message='as senhas devem ser iguais!')])
    cadastrar = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=80)])
    remember = BooleanField('Lembre-me')
    entrar = SubmitField('Entrar')