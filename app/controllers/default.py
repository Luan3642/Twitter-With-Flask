from  app import app, db
from flask import render_template, flash
from flask_login import login_user

from app.models.tables import User
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
       user = User.query.filter_by(username=form.username.data).first()
       if user and user.password == form.data.password:
           login_user(user)
           flash("Logged in ")
       else: 
            flash("invalid login ")
    else:
        print(form.errors)
    return render_template("login.html", form=form)





# @app.route("/teste/<info>")
# @app.route("/teste", defaults={"info": None })

#faz criacao
# def teste(info):
#     i = User("luan", "1234", "LuanMagalhaes", "luan777@hsasail.com")
#     db.session.add(i)
#     db.session.commit()
#     return "Ok"


#faz consulta
# def teste(info):
#     r = User.query.filter_by(username="luan").all()
#     print(r)
#     return "ok"


# DELETE
# def teste(info):
#     r = User.query.filter_by(username="luan").all()
#     db.session.delete(r)
#     db.session.commit()
#     return "OK"
