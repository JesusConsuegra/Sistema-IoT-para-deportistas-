from tinydb import TinyDB, where
from sklearn.cluster import KMeans
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

class handler_ddbb:
	
	def agregar_datos(self, estampa, FC, VFC, sesion):
		db = TinyDB("ddbb.json")
		db.insert({"estampa":estampa, "FC":FC, "VFC":VFC, "sesion":sesion})
	
	def consultar_datos(self):
		db = TinyDB("ddbb.json")
		lista = db.all()
		x = []
		aux=0
		
		for elem in lista:
			y = eval(elem["sesion"])
			
			if elem == 0:
				aux = x.append([y])
			
			if aux != y:
				x.append([y])
				aux = y		
		
		cad = "<table border='2'>"
		for ses in x:	
			cad = cad + "<tr><td>Sesion</td><td>" + str(ses) + "</td></tr>"
		cad = cad+"</table>"
		
		print(x)
		return cad
	
	def consultar_sesion(self, sesion):
		db = TinyDB("ddbb.json")
		lista = db.search(where("sesion") == sesion)
		hr = 0
		rr = 0
		con = 0
		
		cad = "<table border='2'>"
		for elem in lista:
			cad = cad + "<tr><td>Estampa</td><td>" + str(elem["estampa"]) + "</td></tr>"
			cad = cad + "<tr><td>FC</td><td>" + str(elem["FC"]) + "</td></tr>"
			cad = cad + "<tr><td>VFC</td><td>" + str(elem["VFC"]) + "</td></tr>"
			cad = cad + "<tr><td>Sesion</td><td>" + str(elem["sesion"]) + "</td></tr>"
			cad = cad + "<tr><td> </td><td>" "</td></tr>"
			uno =  eval(elem["FC"])
			dos =  eval(elem["VFC"])
			hr = hr + uno
			rr = rr + dos
			con = con + 1
		
		cad = cad + "<tr><td>Promedio FC</td><td>" + str(hr/con)+ "</td></tr>"
		cad = cad + "<tr><td>Promedio VFC</td><td>" + str(rr/con)+ "</td></tr>"
		cad = cad + "<tr><td>Cantidad de datos</td><td>" + str(con)+ "</td></tr>"
		cad = cad + "</table>"
		return cad

	def consultar_estadistica(self, sesion):
		db = TinyDB("ddbb.json")
		lista = db.search(where("sesion") == sesion)
		cad = "<table border='2'>"
		hr = 0
		rr = 0
		con = 0
		maximoHr = 0
		minimoHr = 1000
		maximoRr = 0
		minimoRr = 1000
		estado = ""
		
		for elem in lista:			
			uno =  eval(elem["FC"])
			dos =  eval(elem["VFC"])
			hr = hr + uno
			rr = rr + dos
			con = con + 1
			
			if maximoHr<uno:
				maximoHr = uno
				
			if minimoHr>uno:
				minimoHr = uno
				
			if maximoRr<dos:
				maximoRr =dos
				
			if minimoRr>dos:
				minimoRr = dos
			
		if (rr/con)<750:
				estado = "Alto"
				
		if (rr/con)>900:
				estado = "Bajo"
				
		if ((rr/con)>750 and (rr/con)<900):
				estado = "Moderado" 	
		
		cad = cad + "<tr><td>Sesion</td><td>" + sesion + "</td></tr>"
		cad = cad + "<tr><td> </td><td>" "</td></tr>"
		cad = cad + "<tr><td>promedio ritmo cardiaco</td><td>" + str(hr/con) + "</td></tr>"
		cad = cad + "<tr><td>promedio variabilidad ritmo cardiaco</td><td>" + str(rr/con) + "</td></tr>"
		cad = cad + "<tr><td>Hr+</td><td>" + str(maximoHr) + "</td></tr>"
		cad = cad + "<tr><td>Hr-</td><td>" + str(minimoHr) + "</td></tr>"
		cad = cad + "<tr><td>Rr+</td><td>" + str(maximoRr) + "</td></tr>"
		cad = cad + "<tr><td>Rr-</td><td>" + str(minimoRr) + "</td></tr>"
		cad = cad + "<tr><td>AvRRInterval</td><td>" + estado + "</td></tr>"
		cad = cad + "<tr><td>Cantidad de datos</td><td>" + str(con) + "</td></tr>"
		
		auxHr = []
		auxRr = []
		estado = ""
		
		for elem in lista:
			uno =  eval(elem["FC"])
			dos =  eval(elem["VFC"])
			auxHr.append([uno])
			auxRr.append([dos])
			
		sdrr = np.std(auxRr)
		
		if sdrr < 50:
			estado = "Alto"
		if sdrr > 100:
			estado = "Bajo"
		if (sdrr >=50 and sdrr<=100):
			estado = "Moderado"
		
		cad = cad+"<tr><td>Hr(SDHR)</td><td>" + str(np.std(auxHr)) + "</td></tr>"
		cad = cad+"<tr><td>Rr(SDRR)</td><td>" + str(np.std(auxRr)) + "</td></tr>"
		cad = cad+"<tr><td>SDRR</td><td>" + estado + "</td></tr>"
	
		cont = 0
		pr50 = 0.0
		nex = 0
		estado = ""
		
		for elem in lista:
			uno =  eval(elem["FC"])
			dos =  eval(elem["VFC"])
			if (abs(int(dos) - nex ) > 50):
				cont = cont+1
			nex = int(dos)
		
		pr50 = float(cont) /float(len(lista))*100
		
		if pr50 < 3:
			estado = "Alto"
		else:
			estado = "Bajo"
			
		cad = cad + "<tr><td>pRR50</td><td>" + str(pr50) + "</td></tr>"
		cad = cad + "<tr><td>Nivel de riesgo pRR50</td><td>" + estado + "</td></tr>"
		cad = cad + "<tr><td>Numero de Intervalos </td><td>" + str(cont) + "</td></tr></table>"

		return cad
		
		
	def consultar_centroide(self, sesion ,nC):
		db = TinyDB("ddbb.json")
		lista = db.search(where("sesion") == sesion)
		aux = []
		fc = []
		vfc = []
		x_cen = []
		y_cen = []
		  
		for elem in lista:
			hr=eval(elem["FC"])
			rr=eval(elem["VFC"])
			fc.append([hr])
			vfc.append([rr])
			aux.append([elem["FC"], elem["VFC"]])

		
		kmeans = KMeans(n_clusters = nC)
		kmeans.fit(aux)
		centroides=kmeans.cluster_centers_
		
		lista = []
		for elem in kmeans.labels_:
			lista.append(elem)		
			
		cad = "<table border='2'"
		cad = cad + "<tr><td><center>CENTROIDES</center></td><td><center>HR</center></td><td><center>RR</center></td><td><center>Instancias</center></td></tr>"
		i=1
		instancias=0
		for cen in centroides:
			
			x = int(cen[0])
			y = int(cen[1])
			x_cen.append([x])
			y_cen.append([y])
			numElem = lista.count(instancias)
			cad = cad + "<tr><td> Centroide: "+str(i)+"</td><td>" + str(int(cen[0])) + "</td><td>" + str(int(cen[1])) + "</td><td><center>"+str(numElem)+"</center></td></tr>"
			instancias = instancias +1
			i = i+1
		
		cad = cad + "</table>"	

		plt.scatter(fc,vfc, c=kmeans.labels_, cmap='rainbow')
		plt.scatter(x_cen,y_cen, c="black")
		plt.xlabel("HR")
		plt.ylabel("RR")		
		plt.savefig("static/prueba.png")
		plt.clf()
				
		return cad



	def consultar_centroide2(self, sesion ,nC):
		db = TinyDB("ddbb.json")
		lista = db.search(where("sesion") == sesion)
		aux = []
		est = 0	
		rr = []
		nR = []
		x_cen = []
		y_cen = []		
		con = 0
					
		for elem in lista:
			vfc=eval(elem["VFC"])
			con = con + 1
			
			if vfc >= 750 and vfc <= 900:
				est = 2			
			if vfc < 750:
				est = 3
			if vfc > 900:
				est = 1
		
			rr.append([vfc])
			nR.append([est])
			aux.append([est, elem["VFC"]])
			est =0
			
		kmeans = KMeans(n_clusters = nC)
		kmeans.fit(aux)
		centroides=kmeans.cluster_centers_
		
		lista = []
		for elem in kmeans.labels_:
			lista.append(elem)
		
			
		cad = "<table border='2'"
		cad = cad + "<tr><td><center>CENTROIDES</center></td><td><center>NR</center></td><td><center>RR</center></td><td><center>Instancias</center></td></tr>"
		i=1
		instancias=0
		for cen in centroides:
			NR = 1
			x = cen[0]
			if x >= 1.5 :
				NR = 2
			if x >= 2.5:
				NR = 3
			
			y = int(cen[1])
			x_cen.append([x])
			y_cen.append([y])	
			numElem = lista.count(instancias)	
			cad = cad + "<tr><td> Centroide: "+str(i)+"</td><td><center>" + str(NR) + "</center></td><td>" + str(int(cen[1])) + "</td><td><center>"+str(numElem)+"</center></td></tr>"
			instancias = instancias +1
			i=i+1
		cad = cad + "</table>"
		
		
		plt.scatter(nR,rr, c=kmeans.labels_, cmap='rainbow')
		plt.scatter(x_cen,y_cen, c="black")	
		plt.xlabel("NIVEL DE RIESGO")
		plt.ylabel("RR")			
		plt.savefig("static/prueba.png")		
		plt.clf()
				
		return cad
