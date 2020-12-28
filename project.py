from flask import Flask, render_template
from handler_ddbb import handler_ddbb
import random
import time

app = Flask(__name__)
man = handler_ddbb()

@app.route("/")
def home():
	titulo = "TOMA DE DATOS"
	return render_template("index.html", titulo = titulo)
	
@app.route("/aleatorio")
def aleatorio():
	HR = random.randint(60,100)
	RR = 60000/HR
	estampa=time.time()*1000
	man.agregar_datos(estampa, RR, HR)
	return	"{\"HR\":"+str(HR)+",\"RR\":"+str(RR)+"}"

if __name__ == "__main__":
	app.run("0.0.0.0")
