# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Esta parte é essencial para iniciar o servidor Flask
if __name__ == '__main__':
    # O servidor escutará em todas as interfaces de rede (0.0.0.0)
    # na porta 5000 dentro do contêiner.
    app.run(host='0.0.0.0', port=5000)