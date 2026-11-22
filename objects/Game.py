import json
import pyxel 
import Board

class Game:
    def __init__(self):
     with open("assets/config.json", "r") as file: # abres el archivo
      self.config_data = json.load(file) 
     pyxel.init(
       self.config_data["SCREEN_H"],
       self.config_data["SCREEN_W"],
       title="TABERNA CHACON",
       display_scale=4)


     
        