from flask import Flask, render_template, redirect, url_for, request
from registro import LoginForm, CadastraUsuarioForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SECRET_KEY'] = '8d39132b1bfec3225ad1aa46df64deee'

db = SQLAlchemy(app)


class Usuario(db.Model):
    Id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(80), nullable = False)
    
    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = generate_password_hash(senha)
    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():    
    form = CadastraUsuarioForm()
    if form.validate_on_submit():
        print(form.username.data)
        user = Usuario(email=form.email.data,
        username=form.username.data,
        senha=form.senha.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('cadastro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1> OLá </h1>'

    return render_template('login.html', form=form) 



@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/sistemas-operacionais')
def sistemas():
    return render_template('sistemas-operacionais.html')

@app.route('/programacao')
def progamacao():
    return render_template('programacao.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/apoie')
def apoie():
    return render_template('login.html')
    
if(__name__ == '__main__'):
    app.run(debug=True)
    