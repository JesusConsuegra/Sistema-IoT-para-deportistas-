from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
	titulo = "TOMA DE DATOS"
	return render_template("index.html", titulo = titulo)
	
@app.route("/aleatorio")
def aleatorio():
	HR = random.randint(60,100)
	RR = 60000/HR
	return	"{\"HR\":"+str(HR)+",\"RR\":"+str(RR)+"}"

if __name__ == "__main__":
	app.run("0.0.0.0")
