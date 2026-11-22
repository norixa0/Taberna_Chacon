#!/usr/bin/env python3

# © 2026 Daniel Castro Martín-Romo, Fernando Estaca Fuentes. All rights reserved.

from objects import (
    Board, Chef, Dish, Game, Ingredient, Order, Recipe, Station
    )


'''Nota para fernando

para usar json y abrir el archivo tienes que hacer algo asi:

import json

with open("assets/config.json", "r") as file: # abres el archivo
    self.config_data = json.load(file) # cargas con json (funciona como un dictionary)
    tile = self.config_data["tiles"]    # asignas a la variable tile el valor dentro del json "tiles": 34 
    
'''