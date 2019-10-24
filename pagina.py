from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/apoie')
def apoie():
    return render_template('apoie.html')
    
if(__name__ == '__main__'):
    app.run(debug=True)
    