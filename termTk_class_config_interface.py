from TermTk import TTkUtil, TTkUiLoader, TTkContainer, pyTTkSlot
from class_files_dcc import *

class interfaceConfig(TTkContainer):
    def __init__(self):
        self.configfile = "config/config.json"


        # Data generated using ttkDesigner
        TTkUiLoader.loadDict(TTkUtil.base64_deflate_2_obj(
    "eJyFlNtP2zAUxlOaNr3A2LiNi4byCC9V2aRp7KZBBRsLTJXoxgPbg5N4PRZpXCXOBpOQ9kglP3r/746TNMC2skRRju0cf7/zxfZP85dbNdLrUm1I6xuNYsZDJSuPW+1W" +
    "W8mySJjSQxUvIHGs5HSvd9bhoSAspJGS1SGJyCBOPzE/kAFVsnGEYycs9Pl3JWtdHjOhp/yiNhzDqVBpHrMfNG06zgqV9SMW2ifMF6AcA5Ox9Y6yPgjdrB+R83zwvWGU" +
    "9Dh25ONZj/WJxcwNqLqS1l5IMPJ12OM86LGhkoaSVpf4Pgv7OUN6U1k9JBc8EUrWsaQ8TmQ1yCIsCCqwCtYlFvGW8gEV0UWejtxCxbLmAQv8iOra0s/TmfLKdeIG1OW0" +
    "x8OvrD/ubWqEkjNFYUZHbecBhVnHgPv4PEgLgrnsNX8FC1ewCEvwUH9Zxiy8KazAqqzu8shH+69kpccE1g5LcjqTsPcD0o+1N0YtgbUbZcB6Rt9yZpAebJw1o66l9bs0" +
    "KKDNwD3o5rBTWjSFXdDRrNNA2NIkWGn26Dl62jjo2js+mqPXTKXDA46LxVw7bQ/Q752A9cMBDfUvTmQ5QmPwX5c9Hui3he14SELllKSFfXmcZLBNDYtrb89nouCtiHNR" +
    "AM8VwPMZcOkWMIbXtI2DcJgIu3cxpFquvucBt4+4jy0DnsrZrXa7deNRCbzAgZf4vMJ5Xo+pYGtMUg3cLo9E4V35tnfmXd6hoJklP4NteI7eTFB7M1azsO4bcnOF3Mz/" +
    "Koc9bO2nRZpb28+eTKos9bsD1Dtz+Xnhd9VzD1l8XaWVyy5nssuTZZ/KRfsYcJkGmG8TYceCRCLBfVrrRdhFBFUjaaWKuJFHspmG9nE6MtmSj9f7zdXHU8SDADfIGLCS" +
    "A65ngOt3Aa5lgF4xy01MOB3B5xF8mUiSngG7iRB45I2ZGq7okNCjARkTPXKaOdG9jKh2F1G1Q6NI526OZD31Qx9zSpNM8oOOteuu2PHoUBTSs39K1++StorkzRGc/VuR" +
    "/t1FkkQ20cGQevrwj/GETFq/AUP7/T0="), self)


        self.window = self.getWidgetByName("configWindow")
        self.window.setTitle("Config Panel")

        self.txtIP = self.getWidgetByName("txtIP")
        self.txtPort = self.getWidgetByName("txtPort")
        
        self.cbController = self.getWidgetByName("cbController")
        self.cbList = self.getWidgetByName("cbList")

        self.getWidgetByName("btAceptar").clicked.connect(lambda : self.aceptar_())
        self.getWidgetByName("btCancelar").clicked.connect(lambda : self.cancelar_())

        self.get_JSON_data()


    ## Guarda los datos en el archivo "config/config.json"

    @pyTTkSlot() 
    def aceptar_(self):
 
        files_dcc().updateElementJsonConfigFile(self.configfile, 2, self.txtIP.text())
        files_dcc().updateElementJsonConfigFile(self.configfile, 3, int(self.txtPort.text()))
        files_dcc().updateElementJsonConfigFile(self.configfile, 4, self.cbController.checkState())
        files_dcc().updateElementJsonConfigFile(self.configfile, 5, self.cbList.checkState())


    @pyTTkSlot() 
    def cancelar_(self):
        self.close()

    ## Retorna los datos del archivo /config/config.json
    def get_JSON_data(self):
        ip = files_dcc().getElementJsonConfigFile(self.configfile, 2) # , files_dcc().claves_config[2])
        port = files_dcc().getElementJsonConfigFile(self.configfile, 3) #, files_dcc().claves_config[3])
        showcontroller = files_dcc().getElementJsonConfigFile(self.configfile, 4) #, files_dcc().claves_config[4])
        showlist = files_dcc().getElementJsonConfigFile(self.configfile, 5) #, files_dcc().claves_config[5])
        # showpanel = files_dcc().updateJsonConfigFile("config/config.json", 6, files_dcc().claves_config[6])
        
        self.txtIP.setText(ip)
        self.txtPort.setText(str(port))

        self.cbController.setCheckState(showcontroller)
        self.cbList.setCheckState(showlist)



if __name__  == '__main__':

    # Initialize TTK, add the window widget, and start the main loop
    root=TTk()
    root.layout().addWidget(interfaceConfig())
    root.mainloop()