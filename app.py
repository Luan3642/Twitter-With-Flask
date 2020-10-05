from flask import Flask


# instância do flask, essa instância recebe uma variável
# essa variável vai controlar a aplicação inteira 
app = Flask(__name__)


# decorator, serve pra aplicar uma função encima de outra função.
@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()