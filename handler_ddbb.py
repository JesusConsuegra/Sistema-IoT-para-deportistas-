from tinydb import TinyDB, where

class handler_ddbb:
	
	def agregar_datos(self, estampa, FC, VFC, sesion):
		db=TinyDB("ddbb.json")
		db.insert({"estampa":estampa, "FC":FC, "VFC":VFC, "sesion":sesion})
	
	def consultar_datos(self):
		db=TinyDB("ddbb.json")
		lista=db.all()
		
		cad="<table border='2'>"
		for elem in lista:
			cad=cad+"<tr><td>Estampa</td><td>"+str(elem["estampa"])+"</td></tr>"
			cad=cad+"<tr><td>FC</td><td>"+str(elem["FC"])+"</td></tr>"
			cad=cad+"<tr><td>VFC</td><td>"+str(elem["VFC"])+"</td></tr>"
			cad=cad+"<tr><td>Sesion</td><td>"+str(elem["sesion"])+"</td></tr>"
		cad=cad+"</table>"
		return cad
	
	def consultar_sesion(self, sesion):
		db=TinyDB("ddbb.json")
		lista=db.search(where("sesion")==sesion)
		hr=0
		rr=0
		con=0
		
		cad="<table border='2'>"
		for elem in lista:
			cad=cad+"<tr><td>Estampa</td><td>"+str(elem["estampa"])+"</td></tr>"
			cad=cad+"<tr><td>FC</td><td>"+str(elem["FC"])+"</td></tr>"
			cad=cad+"<tr><td>VFC</td><td>"+str(elem["VFC"])+"</td></tr>"
			cad=cad+"<tr><td>Sesion</td><td>"+str(elem["sesion"])+"</td></tr>"
			cad=cad+"<tr><td> </td><td>" "</td></tr>"
			hr=hr+elem["FC"]
			rr=rr+elem["VFC"]
			con=con+1
		
		cad=cad+"<tr><td>promedio FC</td><td>"+str(hr/con)+"</td></tr>"
		cad=cad+"<tr><td>promedio VFC</td><td>"+str(rr/con)+"</td></tr>"
		cad=cad+"<tr><td>Cantidad de datos</td><td>"+str(con)+"</td></tr>"
		cad=cad+"</table>"
		return cad

