from tinydb import TinyDB, where

class handler_ddbb:
	
	def agregar_datos(self, estampa, FC, VFC):
		db=TinyDB("ddbb.json")
		db.insert({"estampa":estampa, "FC":FC, "VFC":VFC})
	
	def consultar_datos(self):
		db=TinyDB("ddbb.json")
		lista=db.all()
		
		cad="<table border='2'>"
		for elem in lista:
			cad=cad+"<tr><td>Estampa</td><td>"+str(elem["estampa"])+"</td></tr>"
			cad=cad+"<tr><td>FC</td><td>"+str(elem["FC"])+"</td></tr>"
			cad=cad+"<tr><td>VFC</td><td>"+str(elem["VFC"])+"</td></tr>"
		cad=cad+"</table>"
		return cad

