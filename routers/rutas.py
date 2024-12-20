from flask import render_template
import json

def Home(Ruta:str):
    TituloName = Ruta
    return render_template('home.html', TituloName=TituloName)

def Fnaf(Ruta:str):
    TituloName = Ruta
    with open('static/juegosFnaf.json', 'r') as file:
        items = json.load(file)
    return render_template('fnaf.html', TituloName=TituloName, items=items)