import os
import secrets
from PIL import Image
from flask import Flask, render_template, redirect, url_for, request, flash
from forms import LoginForm, CadastraUsuarioForm, UpdateImage
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required,current_user, UserMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SECRET_KEY'] = '8d39132b1bfec3225ad1aa46df64deee'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(80), nullable = False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')


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
    logout_user()   
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UpdateImage()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            db.session.commit()
            

    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)
    return render_template('home.html', image_file=image_file, form=form)

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

    
if(__name__ == '__main__'):
    app.run(debug=True)
    