import os

from functools import wraps
from flask import Flask, render_template, redirect, url_for, request, session
from forms import LoginForm, CadastraUsuarioForm, UpdateImage
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required,current_user, UserMixin
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
    image_file = db.Column(db.String(20), nullable=False, default='default.png')

'''
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in user_id:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login', next=request.url))
        
    return wrap
'''

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
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.senha, form.senha.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', form=form) 

@app.route('/logout')
def logout():
    session.clear()
    logout_user()   
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
    if current_user.is_anonymous:
        return render_template('index.html')
    else:
        return render_template('home.html')
    

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UpdateImage()
    if form.validate_on_submit():
        image = 'img/profile_pics/' + form.picture.data.filename
        form.Trocar_foto.data.save(os.path.join(app.static_folder, image))
        current_user.query.update({ 'image_file': form.Trocar_foto.data.filename })
        db.session.commit()

    user = Usuario.query.filter_by(email=str(current_user.email)).first()
    imagem = 'img/profile_pics/' + user.image_file
    return render_template('home.html', form=form, image=imagem)

@app.route('/sistemas-operacionais')
def sistemas():
    return render_template('sistemas-operacionais.html')

@app.route('/logica')
def logica():
    return render_template('programacao.html')


@app.route('/html')
@login_required
def html():
    return render_template('web.html')

@app.route('/apoie')
def apoie():
    return render_template('apoie.html')

@app.route('/aula1-logica')
def aula1L():
    return render_template('cursos/aula1-logica.html')

@app.route('/aula2-logica')
def aula2L():
    return render_template('cursos/aula2-logica.html')

@app.route('/aula3-logica')
def aula3L():
    return render_template('cursos/aula3-logica.html')

@app.route('/aula4-logica')
def aula4L():
    return render_template('cursos/aula4-logica.html')

@app.route('/aula1-html')
def aula1H():
    return render_template('cursos/aula1-html.html')

@app.route('/aula2-html')
def aula2H():
    return render_template('cursos/aula2-html.html')

@app.route('/aula3-html')
def aula3H():
    return render_template('cursos/aula3-html.html')

@app.route('/aula4-html')
def aula4H():
    return render_template('cursos/aula4-html.html')
  
@app.route('/aula1-so')
def aula1SO():
    return render_template('cursos/aula1-so.html')

@app.route('/aula2-so')
def aula2SO():
    return render_template('cursos/aula2-so.html')

@app.route('/aula3-so')
def aula3SO():
    return render_template('cursos/aula3-so.html')

@app.route('/aula4-so')
def aula4SO():
    return render_template('cursos/aula4-so.html')
  
if(__name__ == '__main__'):
    app.run(debug=True)
    