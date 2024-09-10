from TermTk import TTkUtil, TTkUiLoader, TTkContainer, pyTTkSlot
from class_list_dcc import *
from class_cliente_dcc import *
from TerminalDCC_main import *

# from TermTk import TTk
# import xml.dom.minidom

ID = 0
ADDR = 1
SPEED = 2
DIRECTION = 3

SAVE_SPEED = 0
SAVE_DIRECTIOM = 1
##
# @ data: -> datos
class InterfaceController(TTkContainer):
	def __init__(self, data):
		self.data = data
		self.item_seleccion = ""
		self.name_ = ""
		self.address_ = -1
		self.speed_ = 0
		self.direction_ = 0
		self.speedList = []
		self.current_sel = ""
		self.__dataToMain = ""

        # The "TTkUiLoader" is responsible to init this custom object
        # and extend it to the "textEditWindow" created in this tutorial
        # NOTE: no "super().__init__()" is required

        # Data generated using ttkDesigner

		TTkUiLoader.loadDict(TTkUtil.base64_deflate_2_obj(
    "eJydVN9v0zAQTtUmadr9YGxssEloT2hPpfC2N9hvkQ0mWm0PMKS0tXrW3LhKnK1DGuKxk/xo/l/OdlIGop2gVZS72Of7vu/u/L3yY8dzzO9WbUn/iiQp5bGS7utGs9FU" +
    "siwyqvSS22VRmio5125f7vJYRDQmiZLeMEqiQWq2VN5HA6Jk7QTXzmnc49dKVk95SoU+8kJthaWwRGSlRb8S4zbCNSKDExpvntOeABXWMBi9I0L7IFTo4GI0yhffOU7J" +
    "0YePinX7xT+jKe0wosbS348jtHrabHPO2nSopKOkfxr1ejTum6SO/RPpHUc3PBNKBkgptzPpMWshIXBhHfxbJHFI+ICI5CYPR9xCpbLaBcp6CTHczH5zVIvRHkqjI7cg" +
    "kH7KWkOCoKCu07thmcC8FWOewGJYgkdhGZbw/dgQguUxrIzhCazK+oeEEpTa6BfOSfcsYhnRuvgoEx1kA2tHI2t/k/UW0mRksyXIUIUlGZxG/cKrZbKcYE0wpNzlzISi" +
    "nw6jWG/18VtuZ5ZMFckcJLqmBZd7XwyZcriUk0FimoyDZBxYskT+5ANreQ+YPoBnsC69HZ5oscbSbVOBRYTVDDbuaQ/PreQvwjJKDpu/Kb2TCYHKFOiCjvhIdAcX8EpY" +
    "ZgtvXqu+GAZW67/Dk5U2GWE7+JNDtscy2AXSvdRdpe6kbxws5V0GDeT5Ep8mFu5VIRm8KbB4HdESfJgDWZgAqVkg3iwgsI8zYoK3x3B4B0cPp0PqBzy5jpKizZ7+E3XM" +
    "6E/ipyclU3CYvjiOOoT96nrWud/1QVjJ4Xi69Iuhi3BKM+C49jjp7nLG8Z6pbHxqDnBU3zLajwc4FNi+01Q5K0DUWWePJqRr5qcA4v4XEPgMF/Blak68b1ABmoqJAHMs" +
    "PeZdPuCCXhX9uDyZ/TU7+zPHRS60CLPgN094j+ghre7Fe7nzMH2sQT5UJntFEzbZVyx1ZzZ1fKaSJlkm610exxZfijdg1vgJh5XuPQ=="), self)

        
        # Connect the open routine to the (open)"filePicked" event
        #self.getWidgetByName("btPlan").clicked.connect(self.hola("10"))

		self.window = self.getWidgetByName("TTkWindow")
		self.btnRev = self.getWidgetByName("btReverse")
		self.btnSt = self.getWidgetByName("btStop")
		self.btnFor = self.getWidgetByName("btForward")

		self.btnRev.clicked.connect(lambda : self.Button_Selection(0))
		self.btnSt.clicked.connect(lambda : self.Button_Selection(2))
		self.btnFor.clicked.connect(lambda : self.Button_Selection(1))

		# Lista
		self.listLoco = self.getWidgetByName("lsLocomotive")
		self.listLoco.textClicked.connect(lambda : self.list_Selection())

		self.txtshow = self.getWidgetByName("lbTitle")
		
		self.txtspeed = self.getWidgetByName("lbSpeed")
		self.txtDirection = self.getWidgetByName("lbDirection")
		self.txtDirection.setText("STOP")

		
		self.slspeed = self.getWidgetByName("slSpeed")
		self.slspeed.sliderMoved.connect(lambda : self.setSpeed())
		self.txtspeed.setText(str(self.slspeed.value()))

		try:
			self.Print_Listbox(Class_Listas_DCC().Single_items_list(self.data, 'lc'))
		except Exception:
			self.txtshow.setText("Seleccione plan Rocrail")

	## Obtiene los datos enviados por class main
	def set_dataFromMain(self, dccData):

		# si hay datos en "dccData"
		if dccData:
			pass
			#self.txtshow.setText(str(dccData))
	
	## Manda los datos a la clase main
	def get_dataFromMain(self):
		# Iteramos la lista de velocidades 
		for item in self.speedList:

			# Si la selección actual esta en la lista
			if self.current_sel == item[0]:

				# Construye el comando que se manda a main
				self.__dataToMain = f"<t1 {item[1]} {item[2]} {item[3]}>"# current_sel: {self.current_sel}"
		
		# Retornamos el comando
		return self.__dataToMain

	@pyTTkSlot(int)
    ## Obtiene el valor de velocidad barra scale 
	def setSpeed(self):
		self.txtspeed.setText(str(self.slspeed.value()))
		self.save_data_speedList(self.current_sel, SAVE_SPEED, self.slspeed.value())
	

	@pyTTkSlot(str)
	def Print_Listbox(self, items):
		# Comprueba si el widget tiene alguna lista y si la tiene la borra
		if self.listLoco.items():
			# Elimina la lista de elementos cargados el la lista
			self.listLoco.removeItems(self.lista.items())
		
		elif not self.listLoco.items():	# Crea la lista con los nuevos elementos
			for item in items:
				self.listLoco.addItem(item)

	@pyTTkSlot(int)
	def Button_Selection(self, dir_):
		self.save_data_speedList(self.current_sel, SAVE_DIRECTIOM, dir_)
		self.Direction(dir_)
		self.txtDirection.setText(self.Direction(dir_))
		#main().sendSocketData(str(dir_))
		
	## Selecciona un estado de locomotora
	# @ direc -> int: 0 Reverse; 1 Forward; 2 Stop
	# @ return -> str: Estado de la locmotora
	def Direction(self, direc):
		txt = ""
		if direc == 0:
			self.btnRev.setFocus()
			txt = "Reverse"
		elif direc == 1:
			txt = "Forward"
			self.btnFor.setFocus()
		else:
			txt = "STOP"
			self.btnSt.setFocus()
		return txt
		
	## Evento al seleccionar un elemento de la Lista. Primero 
	## llama a Class_Listas_DCC y obtiene los atributos de cada
	## locomotora
	# @ event: cuando se selecciona una locomotora
	@pyTTkSlot(str)
	def list_Selection(self):
		name = ""
		dcc_addrs = -1
		speed_value = 0
		direction_value = 0
		for i in self.listLoco.selectedLabels():
			nameid = str(i)
			a = Class_Listas_DCC()
			attributes_ = a.get_locomotive(self.data, nameid.removeprefix('Id: '))
			for attribute in attributes_:
				name = attribute['id']
				dcc_addrs = attribute['addr']

		
		# if not self.speedList:
		# 	self.Add_Loco_to_List(False, name, dcc_addrs, speed_value, direction_value)
		# else: 	
		if self.If_Loc_on_list(self.speedList, name) == False:
			self.Add_Loco_to_List(False, name, dcc_addrs, speed_value, direction_value)
			self.Direction(direction_value)
		else:
			speed_value = self.get_data_speedList(name, SAVE_SPEED)
			direction_value = self.get_data_speedList(name, SAVE_DIRECTIOM)

		self.slspeed.setValue(speed_value)
		self.txtspeed.setText(str(speed_value))
		self.txtDirection.setText(self.Direction(direction_value))

		# Establece la selección actual			 	
		self.current_sel = name

		# Ponemos el titulo en self.labeltitle
		self.txtshow.setText(f"{name}  DCC: {dcc_addrs}")

	## Añade un locomotora a la lista de velocidades
	# @ remove -> boolean: True elimina; False añade
	# @ id -> str: Nommbre del elemento
	# @ speed -> int: Velocidad
	# @ direction -> int: Sentido de la marcha 
	def Add_Loco_to_List(self, remove, id, addr, speed, direction):
		if remove:
			pass
		else:
			self.speedList.append([id, addr, speed, direction])

	## Recupera la velocidad de una locomotora que esta en la lista
	# @ name -> str: True elimina; False añade
	# @ data_type -> int: 0=velocidad; 1=sentido de la marcha
	def get_data_speedList(self, name, data_type):
		for loc in self.speedList:
			if name in loc:
				if data_type == SAVE_SPEED:
					return loc[SPEED]
					break
				elif data_type == SAVE_DIRECTIOM:
					return loc[DIRECTION]
					break

	## Guarda las velocidad o sentido de la marcha del elemneto seleccionado
	# @ name -> str: nombre del elemento al que se actualizaran los datos
	# @ type_data -> int: 0=velocidad; 1=sentido de la marcha
	# @ value -> int: velocidad o sentido de la marcha
	def save_data_speedList(self, name, type_data, value):
		for pos, item_ in enumerate(self.speedList):
			if self.current_sel in item_:
				if type_data == SAVE_SPEED:				
					if item_[SPEED] != value:
						self.speedList[pos][SPEED] = value
				elif type_data == SAVE_DIRECTIOM:				
						self.speedList[pos][DIRECTION] = value
				files_dcc().Save_Log(f"GUARDANDO: {name}, {type_data}, {value}")

	## Comprueba si un nombre (id) está en la lista
	# @ lista -> list: lista donde se comprueba si existe el nombre
	# @ name -> str: Nombre del elemento que vamos a busar en la lista
	# @ retur: True si el elemto existe; False si no existe
	def If_Loc_on_list(self, lista, name):
		value = False
		for item in lista:
			if name in item:
				value = True
				break
			else:
				value = False
		return value


if __name__ == '__main__':
	pass
	# Initialize TTK, add the window widget, and start the main loop
	#file = xml.dom.minidom.parse('/home/peyu/snap/Rocrail/Maqueta_modular/plan.xml')
	#root=TTk()
	#root.layout().addWidget(Interface_Locomotive(file))
	#root.mainloop() 
