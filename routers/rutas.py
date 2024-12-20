from flask import render_template


def Home():
    TituloName:str = "Home"
    return render_template('home.html', TituloName=TituloName)