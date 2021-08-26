from flask import Flask, render_template, request
from handler_ddbb import handler_ddbb
from datetime import datetime
from ritmo import ritmo
import flask_restful as restful
import time
import threading
import os
import asyncio

app = Flask(__name__)
api = restful.Api(app)
man = handler_ddbb()

@app.route("/")
def home():
	t = threading.Thread(name='prueba', target=hilo)
	t.start()
	titulo = "TOMA DE DATOS"
	return render_template("indexCorre.html", titulo = titulo)

def hilo():
	r=ritmo()
	address = "E2:92:A9:B6:BE:E4" 
	char_uid = "00002a37-0000-1000-8000-00805f9b34fb"
	
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	
	loop.run_until_complete(r.run(address, loop, char_uid))
	while(r.bandera()==False):
		loop.run_until_complete(r.run(address, loop, char_uid))

class DataUpdate(restful.Resource):

	def _is_updated(self, request_time):
		"""
		Returns if resource is updated or it's the first
		time it has been requested.
		args:
			request_time: lastffa request timestamp
		"""
		return os.stat('data.txt').st_mtime > request_time

	def get(self):
		"""
		Returns 'data.txt' content when the resource has
		changed after the request time
		"""
		request_time = time.time()
		while not self._is_updated(request_time):
			time.sleep(0.5)
		content = ''
		with open('data.txt') as data:
			content = data.readlines()
		con = content[0]
		conte = content[1]
		
		estampa = time.time()*1000
		sesion = str(request.args["sesionU"])
		man.agregar_datos(estampa, con, conte, sesion)
		
		return {'content': con, 'date': conte}
		

class Data(restful.Resource):

	def get(self):
		"""
		Returns the current data content
		"""
		content = ''
		with open('data.txt') as data:
			content = data.read()
		return {'content': content}


api.add_resource(DataUpdate, '/data-update')
api.add_resource(Data, '/data')

@app.route("/consultarT")
def consultarT():
	return man.consultar_datos()

@app.route("/consultarS")
def consultarS():
	sesion = request.args["sesionB"]
	return man.consultar_sesion(sesion)

@app.route("/estadistica")
def estadistica():
	sesion = request.args["sesionE"]
	return man.consultar_estadistica(sesion)

@app.route("/centroides")
def centroides():
	
	sesion = str(request.args['sesionC'])
	nC = int(request.args['Cen'])
	return man.consultar_centroide(sesion,nC)

@app.route("/centroides2")
def centroides2():
	
	sesion = str(request.args['sesionC2'])
	nC = int(request.args['Cen2'])
	return man.consultar_centroide2(sesion,nC)

if __name__ == "__main__":
	app.run(port=5000, debug=True)
	#app.run("0.0.0.0")
