from app import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autocomplete = True) 
    username = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(25), nullable = False)
    
    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = generate_password_hash(senha)

    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)


class Curso(db.Model):
    Id_curso = db.Column(db.Integer, primary_key=True) 
    nome_curso = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.nome_curso

'''
class Endereco(db.Model):
    estado = db.Column(db.String(30), nullable = False)
    cidade = db.Column(db.String(30), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.Id'),nullable=False)
    category = db.relationship('Usuario',backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.cidade


class Login_usuario(db.Model):
    Id_login = db.Column(db.Integer, primary_key = True) 
    email_usuario = db.Column(db.String(100), unique = True, nullable = False)
    nome_usuario = db.Column(db.String(100), unique = True, nullable = False)
    senha_usuario = db.Column(db.String(25), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.Id'),nullable=False)
    category = db.relationship('Usuario',backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.nome

class Conclui(db.Model):
    matricula = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String(80), nullable = False)
    idade = db.Column(db.Integer, nullable = False)

    data_conclusao Date,
    Id_curso Char(5),
    Id_usuario Char(10),
    PRIMARY KEY(Id_curso,Id_usuario),
    FOREIGN KEY(Id_curso) REFERENCES curso (Id_curso),
    FOREIGN KEY (Id_usuario) REFERENCES usuario (Id_usuario)

    def __repr__(self):
        return '<User %r>' % self.nome

class Frequenta(db.Model):
    matricula = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String(80), nullable = False)
    idade = db.Column(db.Integer, nullable = False)

	data_inicio Date NOT NULL,
	Id_curso Char(5),
	Id_usuario Char(10),
	PRIMARY KEY(Id_curso,Id_usuario),
	FOREIGN KEY(Id_curso) REFERENCES curso (Id_curso),
	FOREIGN KEY (Id_usuario) REFERENCES usuario (Id_usuario)

    def __repr__(self):
        return '<User %r>' % self.nome

class Modulo(db.Model):
    Id_modulo = db.Column(db.Integer, primary_key = True) 
    nome_modulo = db.Column(db.String(100), nullable = False)
	curso_id = db.Column(db.Integer, db.ForeignKey('curso.Id_curso'),nullable=False)
    category = db.relationship('Curso',backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.nome_modulo


class Pre_requisito(db.Model):
    matricula = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String(80), nullable = False)
    idade = db.Column(db.Integer, nullable = False)
	Id_modulo Char(5),
	possui_Id_modulo Char(5),
	PRIMARY KEY(Id_modulo,possui_Id_modulo),
	FOREIGN KEY (Id_modulo) REFERENCES modulo (Id_modulo),
	FOREIGN KEY (possui_Id_modulo) REFERENCES modulo (Id_modulo)		

    def __repr__(self):
        return '<User %r>' % self.nome

class Pergunta(db.Model):
    Id_pergunta = db.Column(db.Integer, primary_key = True) 
    pergunta = db.Column(db.String(100), nullable = False)
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.Id'),nullable=False)
    category = db.relationship('Usuario',backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.Id_pergunta
'''