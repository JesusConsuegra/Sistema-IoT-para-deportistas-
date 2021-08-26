import asyncio
from bleak import BleakScanner
from bleak import BleakClient
import asyncio
import platform
import binascii
import sys
import time

i=0
t1=0
t2=0
rr=0
class ritmo:
	band=False
	def prueba(self):
		print("Hola")
	def bandera(self):
		return self.band
	def notification_handler(self, sender, data):
		global i,t1,t2,rr
		datos=data.hex()
		hr=int(datos[2]+datos[3],16)
		print("==============")
		print("HR: ",hr)
		rr = int(60000/hr)
		print("RR: ",rr)
		print("==============")
		f=open("data.txt","w")
		f.write(str(hr)+"\n"+str(rr))
		f.close()
		
	async def run(self, address, loop, char_uid):
		try:
			self.band=False
			async with BleakClient(address, loop=loop) as client:
				x=await client.is_connected()
				print(f"X es {x}")
				await client.start_notify(char_uid, self.notification_handler)
				i=1
				while i>0:  
					await asyncio.sleep(1)
					i+=1
				await client.stop_notify(char_uid)
				self.band=True
					
		except: 
			self.band=False

