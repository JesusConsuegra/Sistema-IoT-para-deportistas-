from tinydb import TinyDB, where

class handler_ddbb:
	
	def agregar_datos(self, estampa, FC, VFC):
		db=TinyDB("ddbb.json")
		db.insert({"estampa":estampa, "FC":FC, "VFC":VFC})
	
