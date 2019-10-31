from flask import Flask, render_template
from cadastro import CadastraUsuarioForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8d39132b1bfec3225ad1aa46df64deee'

@app.route('/')
@app.route('/index')
@app.route('/inicio')
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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastraUsuarioForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.senha.data)
        print(form.email.data)
        
    return render_template('cadastro.html', formulario=form)

@app.route('/apoie')
def apoie():
    return render_template('apoie.html')
    
if(__name__ == '__main__'):
    app.run(debug=True)
    