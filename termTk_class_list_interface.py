from TermTk import TTkUtil, TTkUiLoader, TTk, TTkContainer
from TermTk import pyTTkSlot
from class_list_dcc import *
import xml.dom.minidom


class Interface_Lista(TTkContainer):
    def __init__(self, data):
        self.data = data
        self.item_seleccion = ""
        #self.lista = []
        # The "TTkUiLoader" is responsible to init this custom object
        # and extend it to the "textEditWindow" created in this tutorial
        # NOTE: no "super().__init__()" is required

        # Data generated using ttkDesigner
        TTkUiLoader.loadDict(TTkUtil.base64_deflate_2_obj(
    "eJyVlc9v0zAUx1M1aZqVbus2htgktAOC7TIVpImfF7bxQ8sKkxrBAXFIE2u2mtpV4owNaRISl1by0Ujc+BeRuDOek7Rr2I+SVGn84vh9vu/56fmr/v23qSXXqVwX5hEK" +
    "I8KoFMbDzeZmU4oyj4lUU4YXuFEkxQ3H6e4wyl1CUShFpe+Gbi9KPtHfuj0kxUwL5j4Q6rPPUlQPWES4cvlJrtslu4SE3iZfUGLa9hISVovQtQ/E51jaGiwG6w0ih5gr" +
    "02q5x9nknqaV1Dy8yObTN+Z7EpFOgORAmC+pCyNfDR3GAof0pdCkMA9c3yf0MIFq6Q+Jyr57wmIuhQUhZeNYVIJ0BAFhA69g8xSCeI1YD/HwJFsOurmMRNXDJPBDlMSW" +
    "fC+q4OpVqNKgFq5ja/JNLU2BhnBdjebtRYTnbA3Pw91IgsEL6WNxgJcG+CZexreytCWpw7fxiqhss9CH1A+E4RAOcePlGK9OyMV3UpWzdgNU4rWxOBXndsw5bMZIXaXD" +
    "DwKXptr2zuBK/jKFc3ZZKTRAYfkqhUJ30DEkUU/9bAyEtYOR11UbIYfCTAzYkmEsyiFUBGxq2WOBeppgR31YZZeECe+ycZzG0hxpNDt8Hx2hYEKkysWkQvM6hXhLGJmD" +
    "jQF+NMSPhzF+Ajl/Cvczu4SfX2TWgck81mOcHKFoklzOk+tTyLWcm//mz3S4E4cUCjEHN/Lw2hS4lfm4XwQN6XZC1+tew52abnDQLcKEMkyqaAJp5pGVKci0CgtFuR2w" +
    "fJRWHmlNQZqJg0K5tTq8TQ6pG+R2tVaQO3ZRiItoxMIct16UO3JRZF/f/VPCc3nozBRoFdb3cxU8uEhFVwiBUwA6O4n4eb8LwHIfZL14YdxHGnZjohe3/pxd7HOzbRQg" +
    "Tx1lay3mI9W0qrt0NzO0qyRUk8Olo7rPqPT4MW9jaIWpiLtjEffORZQuT4nQf/388U3iLdBj7LCAwQmsr35s9uAQexFAWfQQ5ZeKQXEsah6jNA0hgiMr3vwLIL6K/g=="), self)

        if data == None:
            self.close()
        # Connect the open routine to the (open)"filePicked" event
        #self.getWidgetByName("btPlan").clicked.connect(self.hola("10"))
        self.getWidgetByName("btPlan").clicked.connect(lambda : self.Button_Selection("plan"))
        self.getWidgetByName("btLevel").clicked.connect(lambda : self.Button_Selection("zlevel"))
        self.getWidgetByName("btLocomotives").clicked.connect(lambda : self.Button_Selection("lc"))
        self.getWidgetByName("btTurnouts").clicked.connect(lambda : self.Button_Selection("sw"))
        self.getWidgetByName("btTrack").clicked.connect(lambda : self.Button_Selection("tk"))
        self.getWidgetByName("btText").clicked.connect(lambda : self.Button_Selection("tx"))
        self.getWidgetByName("btBlock").clicked.connect(lambda : self.Button_Selection("bk"))
        self.getWidgetByName("btSignals").clicked.connect(lambda : self.Button_Selection("sg"))
        self.getWidgetByName("btSensors").clicked.connect(lambda : self.Button_Selection("fb"))
        self.getWidgetByName("btOuts").clicked.connect(lambda : self.Button_Selection("co"))


        self.lista = self.getWidgetByName("lista1")
        
        # Connect the save routine to the (save)"filePicked" event
        self.lista.textClicked.connect(lambda : self.Current_Selection())
        self.txtshow = self.getWidgetByName("txtShow")


    @pyTTkSlot(str)
    def Current_Selection(self):
        data = ""
        for i in self.lista.selectedLabels():
            data += i
            #self.txtshow.setText(data)
            #self.txtshow.config(state='normal')
            #   data += self.lista.get(i)
            #print(data)
            self.Get_List(str(data))


    pyTTkSlot(str)
    def Button_Selection(self, item):
        self.txtshow.setText("")
        self.item_seleccion = item
        self.Print_Listbox(Class_Listas_DCC().Single_items_list(self.data, item))

    ## Imprime el ID de todos los elementos
    def Print_Listbox(self, items):
        # Comprueba si el widget tiene alguna lista y si la tiene la borra
        if self.lista.items():
            # Elimina la lista de elementos cargados el la lista
            self.lista.removeItems(self.lista.items())
        
        # Crea la lista con los nuevos elementos
        for item in items:
            self.lista.addItem(item)

    # Funcion para obtener la lista desde "Select(self, event)" y
    # lo muestra en TextoSeleccion
    # @ name: xml.dom.minidom.Document
    def Get_List(self, name,):

        #print(f"\nName: {name}, type_: {self.item_seleccion}\n")
        #print(type(name))
        name = name.removeprefix('Id: ')
        if self.item_seleccion == "plan":
            self.txtshow.setText(Class_Listas_DCC().get_plan_nice_list(self.data, name))
        
        elif self.item_seleccion == "zlevel":
            self.txtshow.setText(Class_Listas_DCC().get_level_nice_list(self.data, name))

        elif self.item_seleccion == "lc":
            self.txtshow.setText(Class_Listas_DCC().get_locomotives_nice_list(self.data, name))
        
        elif self.item_seleccion == "sw":
            self.txtshow.setText(Class_Listas_DCC().get_turnout_nice_list(self.data, name))

        elif self.item_seleccion == "tk":
            self.txtshow.setText(Class_Listas_DCC().get_tracks_nice_list(self.data, name))

        elif self.item_seleccion == "tx":
            self.txtshow.setText(Class_Listas_DCC().get_texts_nice_list(self.data, name))

        elif self.item_seleccion == "bk":
            self.txtshow.setText(Class_Listas_DCC().get_block_nice_list(self.data, name))

        elif self.item_seleccion == "sg":
            self.txtshow.setText(Class_Listas_DCC().get_signals_nice_list(self.data, name))

        elif self.item_seleccion == "fb":
            self.txtshow.setText(Class_Listas_DCC().get_sensors_nice_list(self.data, name))

        elif self.item_seleccion == "co":
            self.txtshow.setText(Class_Listas_DCC().get_outputs_nice_list(self.data, name))

        else: 
            print(f" ERROR: data: {data}, tipe_: {self.item_seleccion} ")
        

if __name__ == '__main__':
    # Initialize TTK, add the window widget, and start the main loop
    data = xml.dom.minidom.parse('/home/peyu/snap/Rocrail/Maqueta_modular/plan.xml')
    root=TTk()
    root.layout().addWidget(Interface_Lista(data))
    root.mainloop() 
