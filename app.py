from flask import Flask, render_template, redirect, url_for, request, flash
from registro import LoginForm, CadastraUsuarioForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SECRET_KEY'] = '8d39132b1bfec3225ad1aa46df64deee'

db = SQLAlchemy(app)
login_manager = LoginManager(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(80), nullable = False)
    
    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = generate_password_hash(senha)

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():    
    form = CadastraUsuarioForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        senha=form.senha.data
        repita_senha = form.repita_senha.data
        user = Usuario.query.filter_by(email=email).first()
        if user:
            flash('Esse email já existe')
            return redirect(url_for('cadastro'))

        if senha != repita_senha:
            flash('Senhas')
            return redirect(url_for('cadastro'))

        new_user = Usuario(email=email, username=username, senha=generate_password_hash(senha))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('cadastro.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and user.senha == form.senha.data:
            login_user(user)
            flash('Logged in')
            return redirect(url_for('home'))
        else:
            flash('Invalid Login')
            return redirect(url_for('login'))

    return render_template('login.html', form=form) 

@app.route('/logout')
def logout():
    logout_user()   
    return redirect(url_for('home'))

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
    return render_template('apoie.html')
    
if(__name__ == '__main__'):
    app.run(debug=True)
    