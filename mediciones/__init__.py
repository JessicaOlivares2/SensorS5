import sqlite3
from flask import Flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
app = Flask(__name__)

bd = sqlite3.connect(
           "sensor.sqlite",
           detect_types=sqlite3.PARSE_DECLTYPES
       )
bd.row_factory = sqlite3.Row
with open("Distancia.sql") as f:
   bd.executescript(f.read())
bd.close()

@app.route('/mediciones', methods=('POST',))
def mediciones():
        valorStr = request.form['medicion']
        valor = int(valorStr)

        print(valor)
        bd = sqlite3.connect(
                "sensor.sqlite",
                detect_types=sqlite3.PARSE_DECLTYPES
            )
        bd.row_factory = sqlite3.Row
        bd.execute(
            "INSERT INTO valores (valor_sensor) VALUES (?)",
            (valor, ),
        )
       
        bd.commit()
        bd.close()
        return 'ok'


