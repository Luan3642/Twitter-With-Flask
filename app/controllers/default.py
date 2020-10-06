from  app import app 
from flask import render_template


from app.models.forms import LoginForm

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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template("login.html", form=form)