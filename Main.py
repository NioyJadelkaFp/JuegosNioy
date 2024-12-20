from flask import Flask
from routers import rutas

app = Flask(__name__)

@app.route('/')
def Home():
    return rutas.Home()

if __name__ == "__main__":
    app.run(debug=True)