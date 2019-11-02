from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastraUsuarioForm(FlaskForm):
    username = StringField('Usuário',validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email',validators=[DataRequired(), Email(message="Email Inválido!!")])
    senha = PasswordField('Digite a senha',validators=[DataRequired(), Length(min=8, max=80)])
    repita_senha = PasswordField('Repita a senha',validators=[DataRequired(), EqualTo(senha)])
    cidade = StringField('Cidade',validators=[DataRequired(), Length(min=2, max=80)])
    cadastrar = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=80)])
    remember = BooleanField('Lembre-me')
    entrar = SubmitField('Entrar')