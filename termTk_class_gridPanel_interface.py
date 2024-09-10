from tkinter import *
from tkinter import ttk
from class_list_dcc import *
#from main import *
import xml.dom.minidom
try:
    from PIL import Image, ImageTk
except ImportError:
    import Image
ID = 0
ADDRES1 = 1
PORT = 2
STATE = 3
SWITCHED = 4

class Class_Grid_Panel_DCC(Frame):
    # Inicia la clase con los parametros 
    # @ master
    # @ data: archivo xml con los datos
    # @ title: titulo de la pantalla (generalmente no lo uso = "" )
    def __init__(self, master, data, title):
        self.master = master
        self.data = data
        self.title = title

        # Variables de la clase
        self.plan = []
        self.dicts = {}
        self.operableList = []
        self.value_scale = 1
        self.image_resize_ = (25, 25)
        self.image_w = 20
        self.image_h = 20
        self.imagenes = [
                        "-", "|", "/","("
                        # "assets/track2/tk_rect_v_gr_rotated.png", "assets/track2/tk_rect_v_rd_rotated.png",
                        # 'assets/track2/tk_curv_v_gr.png', 'assets/track2/tk_curv_v_rd.png'
                        ]
        self.imagenes_sensores = [
                        "assets/track2/fb_rect_v_rd.png", "assets/track2/fb_rect_v_gr.png",
                        "assets/track2/fb_curv_v_rd.png", "assets/track2/fb_curv_v_gr.png"
                        ]
        self.imagenes_signals = [
                        "assets/track2/sg_rect_v_rd.png", "assets/track2/sg_rect_v_gr.png"
                        ]
        self.imagenes_switchs = [
                        "assets/track2/sw_rect_v_rd.png", "assets/track2/sw_rect_v_gr.png"
                        ]


        Frame.__init__(self, master, borderwidth=2)
        self.grid(row=0, column=1, sticky="NWES")

        self.CreateBtnSelection()
        # self.CreateGrid()

    def CreateBtnSelection(self):

        # Frame: framebtn y Slider para el tamaño de los iconos
        self.framebtn = ttk.Frame(self)
        self.framebtn.grid(row=0, column=0,  padx=2,  ipady=5)
        
        # Estilo de los botones
        btn = ttk.Style()
        btn.configure("estilo.TButton", height=100, foreground="black", font=('Courier', 8,  'bold'))
        
        # Buttons 
        self.bt_refresf=ttk.Button(self.framebtn, style="estilo.TButton", text="Refres", 
                                command=self.Print_scale)

        self.bt_refresf.grid(row=0,  column=1,  sticky='WNS')

        self.size_scale = Scale(self.framebtn,
                                        from_ = 10, to = 1,
                                        orient = HORIZONTAL, command=self.get_value)
        self.size_scale.grid(row=0, column=0, sticky="NSWE")

    def get_value(self, value):
        self.value_scale = int(value)

    # @ value: String 
    def Print_scale(self):
        if self.value_scale > 0:
            a = self.Map_Scale(self.value_scale, 1, 10, 20, 41)
            b = self.Map_Scale(self.value_scale, 1, 10, 25, 44)
            self.image_w = a
            self.image_h = a
            self.image_resize_ = (b, b)
            print(f" a: {a}, b: {b}")
                 
            self.plan = []
            self.framegrid.destroy()
            self.CreateGrid()

    def Map_Scale(self, num, inMin, inMax, outMin, outMax):
        return int(outMin + (float(num - inMin) / float(inMax - inMin) * (outMax - outMin)))


    # Crea la parrilla con los elementos que se van a mostrar  
    def CreateGrid(self):
        # Frame: frameGrid 
        self.framegrid = Frame(self)
        self.framegrid.grid(row=1, column=0,  padx=2,  ipady=5)
        pista = []
        sensor = []
        img = ""
        # Creamos las celdas
        for n in range(0, 22):
            for i in range(0, 9):
                self.plan.append([])
                pista = self.get_elemetns_from_class_list(self. data, 'tk', n, i)
                sensor = self.get_elemetns_from_class_list(self. data, 'fb', n, i)
                signal = self.get_elemetns_from_class_list(self. data, 'sg', n, i)
                switch = self.get_elemetns_from_class_list(self. data, 'sw', n, i)
                if pista:
                    if str(n) == pista["pos_x"] and str(i) == pista["pos_y"]:
                        img = self.selection_Image('tk', pista["type"], pista["ori"])
                elif sensor:
                    if str(n) == sensor["pos_x"] and str(i) == sensor["pos_y"]:
                        img = self.selection_Image('fb', sensor["curve"], sensor["ori"])
                elif signal:
                    if str(n) == signal["pos_x"] and str(i) == signal["pos_y"]:
                        img = self.selection_Image('sg', signal["type"], signal["ori"])
                elif switch:
                    # print("signal x: " + signal["pos_x"] + " signal y: " +signal["pos_y"] + " signal type: " +signal["type"])
                    if str(n) == switch["pos_x"] and str(i) == switch["pos_y"]:
                        img = self.selection_Image('sw', switch["type"], switch["ori"])
                else:
                    img = self.get_image_track("assets/track2/tk_empty.png", "north")

                
                self.grd = Label(self.framegrid, image=img, 
                                            width=self.image_w, height=self.image_h,
                                            #highlightthickness=1, 
                                            highlightbackground = "black")
                self.grd.image = img
                self.grd.bind("<Button-3>", self.do_popup) 
                
                self.plan[i].append(self.grd)

                # print(f"n: {n}, i: {i}")
                if i > 0 and n > 0:
                    self.plan[i][n].grid(row=i, column=n)

    def do_popup(self, event):
        a = Class_Listas_DCC()
        item = a.get_tracks(self.data, self.name)
        ptint(item['id'])
        m = Menu(self.master, tearoff = 0) 
        m.add_command(label ="Cut") 
        m.add_command(label ="Copy") 
        m.add_command(label ="Paste") 
        m.add_command(label ="") 
        m.add_separator() 
        m.add_command(label ="Properties")  
        print(str(event.x_root))
        try: 
            m.tk_popup(event.x_root, event.y_root) 
        finally: 
            m.grab_release() 


    # Obtiene la lista desde la Clase class_list_dcc
    # @ data: xml.dom.minidom.Document
    def get_from_list(self, data):
        # print("get from list")
        a = Class_Listas_DCC()
        tracks = a.Single_items_list(data, 'tk')
        track_list=[]
        for track in tracks:
            track_list = a.get_tracks_list(self.data, track.removeprefix('Id: '))
            # print(f" elemt: {track_list}")
        return track_list
   
    # Obtiene la lista desde la Clase class_list_dcc
    # @ data: xml.dom.minidom.Document
    # @ item: String  - track, sensor, etc..
    # @ x: int - posición eje x
    # @ y: int - posición eje y
    def get_elemetns_from_class_list(self, data, item, x, y):
        a = Class_Listas_DCC()
        if item == 'tk':    # Trak:
            tracks = a.Single_items_list(data, item) # 'tk'
            for track in tracks:
                lista = a.get_tracks(self.data, track.removeprefix('Id: '))
                if lista[0]['x'] == str(x) and lista[0]['y'] == str(y):
                    # print("Se encontro la X e Y!")
                    data = {  "name": lista[0]['id'],
                            "type": lista[0]['type'],
                            "ori": lista[0]['ori'],
                            "pos_x": lista[0]['x'],
                            "pos_y": lista[0]['y'],
                            "pos_z": lista[0]['z'],
                            }
                    if data:
                        return data
                    
        elif item == 'fb':  # Sensors:
            sensors = a.Single_items_list(data, item) # 'fb'
            for sensor in sensors:
                lista = a.get_sensors(self.data, sensor.removeprefix('Id: '))
                if lista[0]['x'] == str(x) and lista[0]['y'] == str(y):
                    # print("Se encontro la X e Y en sensores!")
                    data = {  "id": lista[0]['id'],
                            "type": lista[0]['type'],
                            "ori": lista[0]['ori'],
                            "pos_x": lista[0]['x'],
                            "pos_y": lista[0]['y'],
                            "pos_z": lista[0]['z'],
                            "curve": lista[0]['curve']
                            }
                    if data:
                        return data
        elif item == 'sg':  # Signals:
            signals = a.Single_items_list(data, item) # 'sg'
            for signal in signals:
                lista = a.get_signals(self.data, signal.removeprefix('Id: '))
                if lista[0]['x'] == str(x) and lista[0]['y'] == str(y):
                    # print("Se encontro la X e Y en sensores!")
                    data = {  "id": lista[0]['id'],
                            "type": lista[0]['type'],
                            "ori": lista[0]['ori'],
                            "pos_x": lista[0]['x'],
                            "pos_y": lista[0]['y'],
                            "pos_z": lista[0]['z'],
                            }
                    if data:
                        return data
        elif item == 'sw':  # Signals:
            switchs_ = a.Single_items_list(data, item) # 'sg'
            for switch_ in switchs_:
                lista = a.get_switchs(self.data, switch_.removeprefix('Id: '))
                if lista[0]['x'] == str(x) and lista[0]['y'] == str(y):
                    # print("Se encontro la X e Y en switch!")
                    data = {  "id": lista[0]['id'],
                            "type": lista[0]['type'],
                            "ori": lista[0]['ori'],
                            "pos_x": lista[0]['x'],
                            "pos_y": lista[0]['y'],
                            "pos_z": lista[0]['z'],
                            }
                    if data:
                        return data                                        
        else:
            pass
    

    ## Obtiene la lista de elementos operables
    ## desde la Clase class_list_dcc
    # @ data: xml.dom.minidom.Document
    # @ item: String  - track, sensor, etc..
    # @ x: int - posición eje x
    # @ y: int - posición eje y
    def get_operable_from_class_list(self, data, item):
        a = Class_Listas_DCC()
        if item == 'fb':  # Sensors:
            sensors = a.Single_items_list(data, item) # 'fb'
            for sensor in sensors:
                lista = a.get_sensors(self.data, sensor.removeprefix('Id: '))
                try:
                    for element in lista:
                        if "operable" in element:
                            data = [lista[0]['id'], 
                            lista[0]['addr'], lista[0]['state'], 
                            lista[0]['timer'], lista[0]['counter']]
                            self.operableList.append(data)
                except Exception as err:
                    print("Error: ", err)

        elif item == 'sg':  # Signals:
            signals = a.Single_items_list(data, item) # 'sg'
            for signal in signals:
                lista = a.get_signals(self.data, signal.removeprefix('Id: '))
                try:
                    for element in lista:
                        if "operable" in element:
                            data = [lista[0]['id'], 
                            lista[0]['addr1'], lista[0]['port1'], 
                            lista[0]['state'], lista[0]['manual']]
                            self.operableList.append(data)
                except Exception as err:
                    print("Error \'sg\': ", err)

        elif item == 'sw':  # Switch:
            switchs_ = a.Single_items_list(data, item) # 'sg'
            for switch_ in switchs_:
                lista = a.get_switchs(self.data, switch_.removeprefix('Id: '))
                for element in lista:
                    if "operable" in element:
                        data = [lista[0]['id'], 
                        lista[0]['addr1'], lista[0]['port1'], 
                        lista[0]['state'], lista[0]['switched']]
                        self.operableList.append(data)

        elif item == 'co':  # Oututs:
            switchs_ = a.Single_items_list(data, item) # 'sg'
            for switch_ in switchs_:
                lista = a.get_switchs(self.data, switch_.removeprefix('Id: '))
                for element in lista:
                    if "operable" in element:
                        data = [lista[0]['id'], 
                        lista[0]['addr1'], lista[0]['port1'], 
                        lista[0]['state'], lista[0]['switched']]
                        self.operableList.append(data)
        else:
            pass
    
    
    ## Seleccion de la imagen:
    # @ item_: String - tk, fb, co...
    # @ type_: String - Curve o straight
    # @ ori_:  String - Orientación del objeto - east, west, north, south
    #           datos para pasar a get_image_track
    # @ return: PIL.ImageTk.PhotoImage
    def selection_Image(self, item_, type_, ori_):
        # print(f"type_: {type_}, item: {item_}, ori: {ori_}")
        if item_ == 'tk':
            if type_:
                if type_ == "curve":
                    return self.get_image_track(self.imagenes[2], ori_)
                else:
                    return self.get_image_track(self.imagenes[0], ori_)
        elif item_ == 'fb':
            if type_ != "true":
               return self.get_image_track(self.imagenes_sensores[1], ori_)
            else:
               return self.get_image_track(self.imagenes_sensores[2], ori_)
        elif item_ == 'sg':
            if type_ != "true":
               return self.get_image_track(self.imagenes_signals[1], ori_)
            else:
               return self.get_image_track(self.imagenes_signals[0], ori_)
        elif item_ == 'sw':
            print(type_)
            if type_ != "true":
               return self.get_image_track(self.imagenes_switchs[0], ori_)
            else:
               return self.get_image_track(self.imagenes_switchs[1], ori_)               

    # Tratamiento de la imagen:
    # @ picture: String - Imagen proporcionada por PIL
    # @ ori_: String - Orientación del objeto - east, west, north, south
    #               datos para pasar a get_image_track
    # @ return: PIL.ImageTk.PhotoImage
    def get_image_track(self, picture, ori_):
        # print(f"picture: {picture}, Orientacion: {ori_}")
        ## Abre la imagen
        img_t = (Image.open(picture))

        ## Cambia el tamaño de la imagen
        img_t = img_t.resize(self.image_resize_)#, Image.ANTIALIAS)
        
        ## Cambia la imagen por la transparencia
        img_t = img_t.convert(mode="RGBA")
        
        ## rota la imagen
        if ori_ == "north":
            img_t = img_t.rotate(90)
            # print("norte")
        elif ori_ == "south":
            img_t = img_t.rotate(270)
            # print("Sur")
        elif ori_ == "east":
            img_t = img_t.rotate(180)
        else:
            img_t = img_t.rotate(0)
            # print("NORTE")

        ## Carga la imagen final en PhotoImage
        return ImageTk.PhotoImage(img_t)    

   
if __name__ == '__main__':
   file = xml.dom.minidom.parse('/home/peyu/snap/Rocrail/Maqueta_modular/plan.xml')
   #file = ""
   master = Tk()
   app = Class_Grid_Panel_DCC(master, file, "Database list" ) #,  (500,500))
   app.get_operable_from_class_list(file, "sw")
   app.get_operable_from_class_list(file, "fb")
   app.get_operable_from_class_list(file, "sg")
   print(app.operableList)
   app.mainloop()
