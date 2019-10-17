
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitebd.db'
db = SQLAlchemy(app)


class Curso(db.Model):
    Id_curso = db.Column(db.Integer, primary_key = True) 
    nome_curso = db.Column(db.String(100), nullable = False)
    carga_horaria = db.Column(db.String(25), nullable = False)

	Id_curso Char(5) PRIMARY KEY,
	nome_curso VARCHAR(100),
	carga_horaria VARCHAR(25)

    def __repr__(self):
        return '<User %r>' % self.nome


class Usuario(db.Model):
    matricula = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String(80), nullable = False)
    idade = db.Column(db.Integer, nullable = False)

	Id_usuario Char(10) PRIMARY KEY,
	cpf Char(11) UNIQUE NOT NULL,
	endereço_usuario VARCHAR(100) NOT NULL,
	celular Char(11),
	fixo Char(11),
	data_nascimento Date NOT NULL,
	sexo Char(1) NOT NULL CHECK (sexo = 'M' or sexo = 'F')

    def __repr__(self):
        return '<User %r>' % self.nome


class Login_usuario(db.Model):
     matricula = db.Column(db.Integer, primary_key = True) 
     nome = db.Column(db.String(80), nullable = False)
     idade = db.Column(db.Integer, nullable = False)

	Id_login Char(10) PRIMARY KEY,
	Id_usuario Char(10),
	senha_usuario Char(25) NOT NULL,
	email_usuario VARCHAR(100) NOT NULL,
	nome_usuario VARCHAR(100) NOT NULL,
	FOREIGN KEY (Id_usuario) REFERENCES usuario (Id_usuario)

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
     matricula = db.Column(db.Integer, primary_key = True) 
     nome = db.Column(db.String(80), nullable = False)
     idade = db.Column(db.Integer, nullable = False)

	Id_modulo Char(5) PRIMARY KEY,
	nome_modulo VARCHAR(100),
	Id_curso Char(5),
	FOREIGN KEY(Id_curso) REFERENCES curso (Id_curso)

     def __repr__(self):
         return '<User %r>' % self.nome


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
     matricula = db.Column(db.Integer, primary_key = True) 
     nome = db.Column(db.String(80), nullable = False)
     idade = db.Column(db.Integer, nullable = False)

	cod_pergunta Char(7) PRIMARY KEY,
	Id_usuario Char(10),
	pergunta VARCHAR(100),
	FOREIGN KEY (Id_usuario) REFERENCES usuario (Id_usuario)

     def __repr__(self):
         return '<User %r>' % self.nome

