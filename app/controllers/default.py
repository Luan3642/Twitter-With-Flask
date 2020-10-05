from  app import app 


@app.route("/index")
@app.route("/") 
def index():
    return "hello world"


#podemos passar parametros as rotas
@app.route("/test", defaults={'name': None}) 
@app.route("/test/<name>")
def teste(name):
    if name:
        return "Ola, %s" % name
    else:
        return "Olá, usuário"