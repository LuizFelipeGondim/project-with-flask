
from flask import Flask, render_template, redirect, url_for, request, session
from forms import LoginForm, CadastraUsuarioForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, current_user, UserMixin
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SECRET_KEY'] = '8d39132b1bfec3225ad1aa46df64deee'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
Bootstrap(app)
 

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(80), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/logout')
def logout():
    session.clear()
    logout_user()   
    return redirect(url_for('login'))

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
            return redirect(url_for('cadastro'))

        if senha != repita_senha:
            return redirect(url_for('cadastro'))

        new_user = Usuario(email=email, username=username, senha=generate_password_hash(senha, method='pbkdf2:sha512'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('cadastro.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.senha, form.senha.data):
            login_user(user)
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', form=form) 

    
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

  
if(__name__ == '__main__'):
    app.run(debug=True)
    