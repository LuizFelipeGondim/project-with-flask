from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastraUsuarioForm(FlaskForm):
    username = StringField(
        'Usuário',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    senha = PasswordField(
        'Digite a senha',
        validators=[DataRequired()]
    )
    repita_senha = PasswordField(
        'Repita a senha',
        validators=[DataRequired(), EqualTo(senha)]
    )
    botao = SubmitField('Cadastrar')