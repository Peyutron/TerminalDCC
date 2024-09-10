import socket
import threading
import time
from TerminalDCC_main import *
#from termTk_class_controller_interface import *


## "hilo_cliente" se encarga de de recibir los mensajes desde
## la conexión socket
# @ socket: Recibe el socket desde la clase "Cliente_socket"
class hilo_cliente(threading.Thread):
	def __init__ (self, socket):
		threading.Thread.__init__(self)
		self.socket = socket
		self.SIZE = 1024
		self._dccReceived = ""


	def run(self):
		# La recep
		while True:
			data = self.socket.recv(self.SIZE) #, self.socket.MSG_WAITALL)
			self._dccReceived = data.decode('UTF-8')
			if self._dccReceived == '':
				continue
			else:
				self.set_dccreceived(self._dccReceived)
				# print(f"datos serial: {self.__dccReceived}")
				#return self.dccReceived

	def set_dccreceived(self, data):
		self._dccReceived = data
		# print(f"set dcc {self._dccReceived}")

	def get_dccreceived(self):
		# print(f"get dcc {self._dccReceived}")
		return self._dccReceived


## Cliente para una conexión socket con módulo
## wi-fi ESP-01 configurado con la documentación DCC-EX
## https://dcc-ex.com/support/wifi-at-version.html
# @ ip: str - Dirección IP de la central DCC
# @ port: int - Puerto de comunicación 2560 para DCC
# @ n_cliente: int - Número de cliente
class Cliente_socket():
	def __init__ (self, ip, port, n_cliente):
		self.ip = ip
		self.port = port
		self.n_cliente = n_cliente
		self.FORMAT = 'UTF-8'
		self.h1 = ""

	## Inicia la conexión con socket
	# return: str - "info_connection"	
	def iniciar(self):
		try:
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
			# Se utiliza ""connect_ex" para tener una confirmación de la conexión
			OkConn = self.client.connect_ex((self.ip, self.port))

			# Si la conexión se realiza con exito (0) inicia "hilo_cliente"
			if OkConn == 0 :
				info_connection = f"[CONNECTED] to DCC station {self.ip}:{self.port}"
				files_dcc().Save_Log(f"{info_connection}")
				self.h1 = hilo_cliente(self.client)
				self.h1.start()
			else:
				info_connection = f"Error al conectar {self.ip}:{self.port}"

			return info_connection

		
		except Exception as er:
			error =  f"Excepcion al conectar: class cliente dcc: {er}"
			files_dcc().Save_Log(f"{error}")
			time.sleep(3)
			return error

	
	def clientSendData(self, data):
		try:
			self.client.send(data.encode(self.FORMAT))
		except Exception as error:
			return ("error enviando datos:", error)

	def get_client_data(self):
		# print(f"datos get client {self.h1.get_dccreceived()}")
		return self.h1.get_dccreceived()
	


	def clientStop(self):
		try:
			self.client.shutdown(socket.SHUT_RDWR)
			return "Socket closed"
		except Exception:
			return "Socket closed"
		self.client.close()


if __name__ == '__main__':
	cliente = Cliente_socket("192.168.1.45", 2560, 1)
	cliente.iniciar()
