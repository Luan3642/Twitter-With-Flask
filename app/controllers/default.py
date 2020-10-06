from  app import app 
from flask import render_template

@app.route("/index")
@app.route("/") 
def index():
    return render_template('index.html')

#podemos passar parametros as rotas
# @app.route("/test", defaults={'name': None}) 
# @app.route("/test/<name>")
# def teste(name):
#     if name:
#         return "Ola, %s" % name
#     else:
#         return "Olá, usuário"


@app.route("/login")
def login():
    return render_template("login.html")