import json 
import os
import xml.dom.minidom
import logging


class files_dcc():
	def __init__(self):
		self.claves_config = ['file_config', 'file_plan', 'ip', 'port', 'showcontroller', 'showlist' ]

	## Abre el archivo plan Rocrail
	# @ filename: str -> directorio donde se aloja el archivo de configuración 
	# @ return TextIO -> Retorna el contenido del archivo XML
	def OpenFileRocrail(self, filename):
		try:
			return open(filename, 'r', encoding='UTF-8')
		except Exception as error:
			print("Ocurrio un error al cargar el plan de rocrail", error)
			return None

	def getDataXML(self, filename):
		try:
			return xml.dom.minidom.parse(filename)

		except Exception as error:
			print("Error en la lectura del plan.xml\n" , error)
			return None

	## Abre el archivo de configuración en formato JSON
	# @ filename: str -> directorio donde se aloja el archivo de configuración 
	# @ return dict -> Retorna los valores de JSON como un diccionario
	def openFileConfigJSON(self, filename): 
		try:
			# Abre el archivo JSON
			jsonFile = open(filename, 'r', encoding='utf-8')
			
			# Lee los datos en formato JSON
			jsonDatas = json.loads(jsonFile.read())

			# Cierra el archivo JSON
			jsonFile.close

			# Retorna los datos en formato JSON
			return jsonDatas

		# con error retorna None	
		except Exception as x:
			print("openJSON: imprime excepcion", x)
			return None	

	## Guarda los datos de configuración en un archivo JSON
	# @ filename: str -> directorio donde se aloja el archivo de configuración 
	# @ configData: dict -> Diccionario con los valores en formato JSON
	def writeJSON(self, filename, configData):
		try:
			# Abre el archivo JSON 
			jsonFile = open(filename, 'w+', encoding='utf-8')
		
			# Escribe el archivo JSON con una indentación de 4 bonito :) 
			#jsonFile.write(json.dumps(configData, indent=4, sort_keys=True, default=str))
			jsonFile.write(json.dumps(configData, indent=4, default=str))
			# Cierra el archivo JSON
			jsonFile.close()
		
		except Exception as error:
			print("Ocurrio un error al guardar config.json", error)

	## Actualiza el archivo de configuración
	# @ filename: str -> directorio donde se aloja el archivo de configuración 
	# @ option: int -> Número de opcion:
	#					0-> file_config
	#					1-> file_rocrail
	#					2-> ip
	#					3-> port
	#					4-> showController
	#					5-> showlist
	# @ inputdata: str -> Datos que se actualizarán
	def updateElementJsonConfigFile(self, filename, option, inputdata):
		configData = ""
		# Abre el archivo JSON 
		configData = self.openFileConfigJSON(filename)
		
		# Sustituye valor del contenido en el buffer
		configData[self.claves_config[option]] = inputdata

		# Guarda los datos en un archivo JSON
		self.writeJSON(filename, configData) 
	
	## Devuelve un elemento del archivo de configuración
	# @ filename: str -> directorio donde se aloja el archivo de configuración 
	# @ option: int -> Número de opcion:
	#					0-> file_config
	#					1-> file_rocrail
	#					2-> ip
	#					3-> port
	#					4-> showController
	#					5-> showlist
	# @ searchdata: str -> Clave de la queremos el valor
	# @ return: valor de la clave
	def getElementJsonConfigFile(self, filename, option): #, searchdata):
		configData = ""
		# Abre el archivo JSON 
		configData = self.openFileConfigJSON(filename)
		
		# obtiene el valor de la clave en el contenido en el buffer
		data = configData[self.claves_config[option]]

		# Guarda los datos en un archivo JSON
		self.writeJSON(filename, configData) 

		return data
	
	## Crea un archivo de configuración como archivo JSON config/config.json
	# @ return dict -> Retorna los valores de JSON como un diccionario
	def createConfigJson(self):
		try:
			# Comprueba si existe el directorio, si no existe lo crea
			if os.path.exists("config"):
				print("directorio OK")
			else:
				print("directorio config no existe, creando...")
				os.mkdir("config")
	
			filename="config/config.json"
	
			# crea el archivo de configuración y carga los datos JSON
			configData = {
	    			"file_config": "config/config.json",
	    			"file_plan": "None",
	    			"ip": "1.1.1.2",
	    			"port": "2560",
    				"showcontroller": 0,
    				"showlist": 0
					}
	
			print("Creando archivo de configuración...")
	
			# Guarda los datos en un archivo JSON
			self.writeJSON(filename, configData)

			# Retorna un diccionario JSON
			return self.openFileConfigJSON(filename)

		except Exception as error:
			print("Ocurrio un error al crear config.json", error)
			return None

	def Save_Log(self, str_):
		logging.basicConfig(filename='termDCC_info.log', encoding='utf-8', level=logging.INFO)
		logging.info(str_)


if __name__ == '__main__':
	
	# a = files_dcc().openJSON('config/config.json', 0)
	# print("Lista:\n", a)

	# a = files_dcc().updateJsonConfigFile('config/config.json', 2, "1.1.1.2")
	# print("Lista:\n", a)

	a = files_dcc().updateJsonConfigFile('config/config.json', 2, "10.10.10.20")
	# print("Lista:\n", a)
	