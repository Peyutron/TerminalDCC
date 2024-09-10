from TermTk import TTkUtil, TTkUiLoader, TTkContainer

class aboutTermtkDCC(TTkContainer):
    def __init__(self):
    	TTkUiLoader.loadDict(TTkUtil.base64_deflate_2_obj(
    "eJyFkktvEzEQgDfNY7MNFY+WV5HQHnMhCqgSQjwkSAsIN6Wiq/bEwdm1MlY3drRrQ4NUiWOQ5mj+KmfGuwsqJ2xZnpc983n8vfPz10ZQjUs3xPCLKEqplcPuk9F4NHbY" +
    "NlY67+qmOS9Lh9eS5HyileFSicJhb8kLviirkM4RXwiHm1PynUmV6a8O+8e6lMZf+dkNWcR6Ajsn8puo1H22LTCaShWfycyAYwEdJu29kHMwXo2m/KJxfgiClveTofHX" +
    "lvBUlnKWC7fG8EBxkjIvJlrniVw6DByGxzzLpJpXSYN6Cuwd8pW2xmFESI1ssZfXEgFBF3YhvCSId0IvhClWzXGq27gS+ynIPCuEZ6vCq5sacn9wCNE/poHP32UbAra8" +
    "9IxtCbjOArhB62ZFA7fqbXsNO2u4DXfgro9ss5afAu7DLvbe6CKjt19jN5GGwPHe6xmVHCeiWEjF83h/MolPH41Hj6ldde74bc7npX+xoG/hwRU4eFgzPWURMUH8B2VA" +
    "dSfiwhxk0vyFCY3gPlWDUpVUoeyx8L8oODikPxMf2cWMqv+BO1fU+MTwwvgW+aZ/EjyLP6p8RYybU5sbGftYt7bYLughKaad6tzvIenlkivHWhiSrZEtt/CcSnlB6yVr" +
    "wavKZHGQaqVE6j9kSV2zo9/8Jv8R"), self)

    	self.window = self.getWidgetByName("teabout")


    	text = """Terminal DCC V-0.1
            \nCreated by: Peyutron
			\nhttps://github.com/Peyutron?tab=repositories
			\nhttps://www.infotronikblog.com
			"""
    	self.window.setText(text)

