from flask import Flask
from routers import rutas

app = Flask(__name__)

@app.route('/')
def Home():
    return rutas.Home("Home")
@app.route('/fnaf')
def Fnaf():
    return rutas.Fnaf("Fnaf")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')