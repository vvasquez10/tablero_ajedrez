from tkinter.messagebox import NO
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def paginaInicial():
    """
    hobbies = ["Futbol", "Programar", "Peliculas"]
    return render_template("index.html", nombre="Victor", apellido="Vasquez", hobbies=hobbies )
    """
    return "Hola Mundo"

@app.route('/<int:row>', methods=['GET'])
def dibujaTablero1(row):
    column=8
    return render_template("index.html", row=row, column=column)

@app.route('/<int:row>/<int:column>', methods=['GET'])
def dibujaTablero2(row, column):
    return render_template("index.html", row=row, column=column, color1="red", color2="black")

@app.route('/<int:row>/<int:column>/<color1>/<color2>', methods=['GET'])
def dibujaTablero3(row, column, color1, color2):
    return render_template("index.html", row=row, column=column, color1=color1, color2=color2)



if __name__ == "__main__":
    app.run(debug = True)