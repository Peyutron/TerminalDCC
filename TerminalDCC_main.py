# from TermTk import TTkUtil, TTkUiLoader, TTk, pyTTkSlot, TTkContainer
from TermTk import *
from class_files_dcc import *
from class_cliente_dcc import *
from termTk_class_controller_interface import *
from termTk_class_list_interface import *
from termTk_class_config_interface import *
from termTk_class_about_interface import *

import threading

import os
import time

class main(TTkContainer):

    def __init__(self, root, data, filename):
        self.root = root 
        self.data = data
        self.filename = filename
        self.configPath = "config/config.json"
        self.conn = ""

        if self.filename == None:
            self.filename = "Select Rocrail plan"
        self.__Alive = False
        self.__onoffdcc = False
        self.showinfodcc = False


        # Data generated using ttkDesigner
        TTkUiLoader.loadDict(TTkUtil.base64_deflate_2_obj(
    "eJytlc1v0zAUwFO6Nv3YGJ+bAGnKgcO4DBgHJGAHVjY+sm4TqxhicHATM1tz4ipxYEVC4thJviCZP4b/jmfHyVa2TjusVRQ/+/m933t+fvk19eev65jfT7Uo3W84SSmP" +
    "lawtLz1aeqRkVWRU6aVawFCaKjnd6x10eCwQjXGiZH2AEhSlRmVqE0VYyVYX1nZpHPLvSja2eUqFNvlFLfoVv4Ll1A79gY3427+PZbNLY2+XhoIo34HNIL3BdJ8ILTa7" +
    "6NAuvnOcil6HCbuez7gfaEr7DKuRdNdiBKNQD3ucsx4dKOko6W6jMKTxvnHq5H8s6xtoyDOhZBNCsuNM1lk+goBIjdwl7k8I4jXmERbJ0G4HbqFS2QgIZWGCdWxG3Viy" +
    "keuNi6Q5NtXW/qvgm8zoEfc9TGZ9h1yD57qJhtzIXzdH5NaI3CZzZN7mzeSO3CF3ZX2VJyHkfiRrPSogcDInp3MX3jpD+6lOjNPIyL0TMZCFHD3yFwCdeGA1X60XoDNB" +
    "caqMB9zCOv4VC/vQn78gbJFgDXs2BNiyEJmsJpAZOOlqwJl+uyCnAxQrvyJdmLPjbDItTYWlfVjSrlwi7coxLXkG5p7D88KvkJXzqAIeRWUO71gq5tcujQpsjR2kKbTV" +
    "TAi4agWO2xcBw5C/HORpWXktv6pBXACpTgKRUz18CLej1slNPBjJZofg4EBfMXUkXSPAZTuakBbZBiJtYy2komRqCJjBZsZmp4B6eoHsyPYGZNfbzKK+uQG3TojejkCJ" +
    "0NdcN473GIXeVsyGoNXqZkxQT+uq0Xm0WmOMdobhFMehPk0Uhxa5o2+iQZ7Xo1kwcw2eAhmGllc2Ph8+7u89WY6gK76NB5nwesMB1qXdXAsI97o8BMkhH8ncpNraKVBa" +
    "faFRmA4i59grOdo5R30CB1TVR2i7WEfw4Ih8OiJ7ZxwaPmtKuhGOs1WUQIeDjwEf5J2e4a9CmdIr8YyerT/rcZ3q7pS7S49V3aj/cpiFqNR7g9mg1IPGHOBYwPGO2Z81" +
    "3x99vxLOGKzaza3OialPo/9cNc2uvEVYZxtGOK25n9AQeg1mhWZtO5esKpa1xHx2xrDaUT8GKBxA7RUbrwKSnoGvnre1vn6GM70rDIJUF2yxq/6q04GCPfaXpafOA2WZ" +
    "bAel9RRYsqV/cx2CYA=="), self)

        self.main_dcc_window()
        self.bar_buttons()
        self.main_buttons()
        self.monitor_container()
    
    ## Carga los widgets de la pantalla principal
    def main_dcc_window(self):

        self.mainWindow = self.getWidgetByName("TTkWindow")
        self.mainWindow._btnClose.clicked.connect(lambda : TTkHelper.quit())

        self.mainWindow.setTitle(self.ponerTitulo(self.filename))
        self.mainWindow.setFocus()

    ## Carga los botones del menu superior
    def bar_buttons(self):

        self.fileMenu = self.getWidgetByName("menuButton")
        self.fileMenu.addMenu("Open").menuButtonClicked.connect(self.showFileDialog_)
        self.fileMenu.addMenu("Config").menuButtonClicked.connect(self.showConfigDialog)
        self.fileMenu.addMenu("Exit").menuButtonClicked.connect(lambda : TTkHelper.quit())

    ## Carga los botones para mostrar/ocultar las 
    ## pantallas controller dcc y list dcc
    def main_buttons(self):
        self.about = self.getWidgetByName("mbAyuda")
        self.about.menuButtonClicked.connect(lambda : self.callClassAbout())

        self.class_list = self.getWidgetByName("classlist")
        self.class_list.menuButtonClicked.connect(lambda : self.callClassList())
        self.container_list = self.getWidgetByName("containerlist")
        self.container_list.hide()

        self.class_controller = self.getWidgetByName("classcontroller")
        self.class_controller.setChecked(True)
        self.class_controller.menuButtonClicked.connect(lambda : self.callClassController())
        self.container_controller = self.getWidgetByName("containerloco")
        # self.container_controller.hide()

        # Carga las interfaces
        self.load_interfaces()

       # Encender apagar central DCC mbnstartdcc
        self.btnstartdcc = self.getWidgetByName("mbndccstart")        
        self.btnstartdcc.menuButtonClicked.connect(lambda : self.startDCC())

        # Conexión Wifi mbnconectar
        self.class_cliente = self.getWidgetByName("mbnconectar")        
        self.class_cliente.menuButtonClicked.connect(lambda : self.conexionWifiOnOff())

        # Activa el hilo para la comunicación
        self.hiloDCC = threading.Thread(target=lambda : self.connection(), daemon=True)
        
        # Inicia hilo DCC
        self.hiloDCC.start() #
        
        # Comprueba que el daemon esta activado
        #print(self.hiloDCC.is_alive()) 

    def monitor_container(self):
        
        self.monitorDCC = self.getWidgetByName("textedit")
        self.monitorDCC.setText("")
        
        self.cleanconn = self.getWidgetByName("btclean")
        self.cleanconn.clicked.connect(self.cleanConn)

        self.sendCommandline = self.getWidgetByName("lesendcommand")
        self.sendCommandline.returnPressed.connect(self.sendLine)

        self.btnSendLine = self.getWidgetByName("btsendline")
        self.btnSendLine.clicked.connect(self.sendLine)


    ## Añade el titulo y el nombre del archivo Rocrail
    ## en la barra de ventana pricipal
    # @ filename: str -> Ruta y nombre del archivo
    # @ return: Devuelve el titulo y     
    def ponerTitulo(self, filename):
        return f"Terminal DCC  -  Plan: {filename}"

    ## Carga cada interface en su container
    def load_interfaces(self):

        self.iLista = Interface_Lista(self.data)
        self.container_list.addWidget(self.iLista)

        self.iController = InterfaceController(self.data)
        self.container_controller.addWidget(self.iController)

    # Abre file picker para seleccionar archivo
    pyTTkSlot()
    def showFileDialog_(self):
        filePicker = TTkFileDialogPicker(pos = (3,3), size=(75,24), caption="Selecciona Archivo Rocrail", path=".", fileMode=TTkK.FileMode.AnyFile ,filter="Archivo Rocrail (*.xml);;Todos (*)")
        filePicker.pathPicked.connect(self._openFilePlan)
        TTkHelper.overlay(None, filePicker, 20, 5, True)

    ## Abre el archivo plan
    def _openFilePlan(self, filePath):
        # Pone la dirección del archivo en la parte superior de la ventana
        self.mainWindow.setTitle(self.ponerTitulo(filePath))

        # Actualiza el archivo config.json opción 1 -> ubicación plan Rocrail
        files_dcc().updateElementJsonConfigFile("config/config.json", 1, filePath)

        # Obtiene los datos xml del plan rocrail
        self.data = files_dcc().getDataXML(filePath)
        
        # Recarga las interfaces
        self.load_interfaces()

    pyTTkSlot()
    def showConfigDialog(self):
        a = interfaceConfig()
        TTkHelper.overlay(None, a, 2, 2, False)
        
    @pyTTkSlot(str)
    def callClassList(self):
        if self.class_list.isChecked():
            self.container_list.show()
        else:
            self.container_list.hide()

    @pyTTkSlot(str)
    def callClassController(self):
        if self.class_controller.isChecked():
            self.container_controller.show()
        else:
            self.container_controller.hide()

    def callClassAbout(self):
        a = aboutTermtkDCC()
        TTkHelper.overlay(None, a, 15, 6, False)
    ## Envía el comando de una sola linea
    @pyTTkSlot()
    def sendLine(self):
        if self.__Alive:
            command = str(self.sendCommandline.text())
            self.sendSocketData(command)

    ## MenuButton: mbnstartdcc 
    ## Envia el comando de encendido o apagado  
    @pyTTkSlot()
    def startDCC(self):
        if self.__Alive:
            if self.btnstartdcc._checked:
                self.sendSocketData("<1>")
            else:
                self.sendSocketData("<0>")
        else:
            self.btnstartdcc.setChecked(False)
            self.printConection("Not connected to server DCC", False)

    ## MenuButton: mbnconectar 
    ## Inicia la conexión con el socket  
    @pyTTkSlot()
    def conexionWifiOnOff(self):
        info = ""
        if self.class_cliente._checked:
            try:

                # Obtiene la ip desde el archivo de configuración
                ip = files_dcc().getElementJsonConfigFile(self.configPath, 2) #, searchdata)

                # Obtiene el puerto desde el archivo de configuración (str to int)
                port = int(files_dcc().getElementJsonConfigFile(self.configPath, 3))
                self.cliente = Cliente_socket(ip, port, 1)
                
                # Inicia el cliente de comunicación y guarda la respuesta en "info"
                info = self.cliente.iniciar()
                
                # Si "info" contiene la palabra CONECTADO, continua
                if "CONNECTED" in info:
                    
                    # Flag de socket activo = True
                    self.__Alive = True
                    self.class_cliente.setText("Connection ON")
                    time.sleep(0.5)
                    self.sendSocketData("<s>")

                else:
                    
                    # Si la conexión falla mbconectar checked = False
                    self.class_cliente.setChecked(False)
                    self.class_cliente.setText("Connection OFF")
                    
                self.showinfodcc = True
                self.printConection(info, False)

            except Exception as error:
                self.printConection(f"no se encontro el servidor, {error}, info: {info}", False)
                return

        else:
            # Para la comunicación llamando a clientStop en class_cliente_dcc
            confirmation = self.cliente.clientStop()

            # Flag de socket activo = False
            self.__Alive = False
            self.class_cliente.setText("Connection OFF")

            # Pone en el texo de respuesta en el label de comunicación
            self.printConection(confirmation, True)


    def connection(self):
        dccDataOld = ""
        iControllerDataOld = ""
        while True:

            # Si el socket esta activo:
            if self.__Alive:
                # Obtenemos los datos del cliente
                dccData = self.cliente.get_client_data()

                # Si hay datos dentro de dccData:
                if dccData != dccDataOld:

                    dccDataOld = dccData

                    # Envía los datos string a checkDataDcc 
                    self.printConection(self.checkDataDCC(dccData), True)

                iControllerData = self.iController.get_dataFromMain()
                if iControllerData != iControllerDataOld:
                    iControllerDataOld = iControllerData
                    self.sendSocketData(iControllerData)
                else:
                    pass
                    
            time.sleep(0.2)
     
    ## Envia datos de comunicación DCC 
    ## a class_cliente_dcc
    def sendSocketData(self, dccData):
        self.cliente.clientSendData(dccData)
        self.printConection(dccData, False)
    

    # Comprueba los datos recibidos del socket
    def checkDataDCC(self, datas):        
        #self.printConection(f"Chekeo de datos: {data}")
        if self.showinfodcc:
            self.showinfodcc = False
            return datas
        else:    
            if "p" in datas:
                if "1" in datas:
                    return "DCC Station On"
                else:
                    return "DCC Station Off"        
            elif "l" in datas:
                pass
            elif "T" or "l" in datas:
                data = datas.split(" ")
                if self.container_controller:
                    self.iController.set_dataFromMain(data)
                    return datas 
           
            elif "DCC" in datas:
                return datas
    
    ## Imprime los mensajes en ""
    def printConection(self, data, in_out):
        try: 
            data = data.strip()
        except Exception:
            pass
        # Datos de entrada "<"
        if in_out:
            data = "<-- " + data
        else:
            data = "--> " + data

        self.conn = self.monitorDCC.toAnsi()
        if self.conn == "":
            self.conn = data
        else:
            data += "\n" + self.conn
            self.monitorDCC.setText(data)
        files_dcc().Save_Log(f"{data}")


    ## Limpia la pantalla de comunicaciónes
    @pyTTkSlot()
    def cleanConn(self):
        self.monitorDCC.setText("")

if __name__  == '__main__':
    #plan = '/home/peyu/snap/Rocrail/Maqueta_modular/plan.xml'
    data = None
    path = None
    config_file = files_dcc().openFileConfigJSON('config/config.json')
    if config_file == None:
        print("Ocurrio un error al cargar el archivo \"config/config.json\"\nCreando nuevo...")
        files_dcc().Save_Log(f"TermTk_main error: Ocurrio un error al cargar el archivo \"config/config.json\"\nCreando nuevo...")

        config_file = files_dcc().createConfigJson()

    plan_file = config_file["file_plan"]
    path = os.path.join(plan_file)         
    datafile = files_dcc().OpenFileRocrail(plan_file)
        
    if datafile == None:
        print("\nOcurrio un error al cargar el plan rocrail, seleccione el correcto")
        files_dcc().Save_Log("TermTk_main error: \nOcurrio un error al cargar el plan rocrail, seleccione el correcto")    
    else:
        data = files_dcc().getDataXML(path)

    print(f"Iniciando interfaz...")    
    time.sleep(2)
    root=TTk()
    root.layout().addWidget(main(root, data, path))
    root.mainloop()