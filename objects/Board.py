#!/usr/bin/env python3

# © 2026 norixa0, albertochamaquito8-create. All rights reserved.

import json
import pyxel, os
from objects.Chef import Chef
from objects.Ingredient import Ingredient

class Board:
    def __init__(self):
        """ Method that creates the board. Additional parameters can be modified through assets/config.json
        """
        with open("objects/assets/config.json", "r") as file: # Read config.json
            self.__config_data = json.load(file)

        # Define parameters (obtains them from json file)
        self.__width = self.__config_data["SCREEN_W"] # Screen width
        self.__height = self.__config_data["SCREEN_H"] # Screen height
        self.__kitchen_map = self.__config_data["KITCHEN_MAP"] # Kitchen map (9 rows, 12 columns)
        self.__tiles = self.__config_data["TILE"] # Tile size in pixels (16x16 default)
        self.__service_h = self.__config_data["SERVICE_H"] # Service area height in pixels

        # Image parameters to draw later:
        # The lists in json file is in format: [bank, row, column, width, height]
        self.__scenery_images = self.__config_data["SCENERY_IMAGES"] # Scenery images in format. 
        self.__chef_images = self.__config_data["CHEF_IMAGES"] # Chef images in format.

        # The board contains two Chefs
        self.chef1 = Chef(self.width // 4, self.height // 4, "upper")
        self.chef2 = Chef(self.width * 3 // 4, self.height * 3 // 4, "lower")

        # List of ingredients, assign them an object and append them to self.ingredients.
        NAMES = ('chorizo', 'potato', 'onion', 'tomato', 'eggs')
        self.ingredients = []
        for ingredient in NAMES:
            ingr = Ingredient(ingredient)
            self.ingredients.append(ingr)

        # Initialize pyxel
        pyxel.init(self.width, self.height, title="TABERNA CHACON", display_scale=4)
        # Loading the pyxres file with the images
        pyxel.load("assets/resources.pyxres")
        # Running the game, this will call the update and draw methods every frame (30fps)
        pyxel.run(self.update, self.draw)

    # ---- PROPERTIES ----
    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height
    
    @property
    def kitchen_map(self) -> list:
        return self.__kitchen_map

    @property
    def tiles(self) -> int:
        return self.__tiles

    @property
    def service_h(self) -> int:
        return self.__service_h

    @property
    def scenery_images(self) -> dict:
        return self.__scenery_images

    @property
    def chef_images(self) -> dict:
        return self.__chef_images

    # ---- METHODS ----

    def update(self):
        """Pyxel method that gets executed in every iteration of
        the game (30fps). It contains the logic to exit the
        program if Q key is pressed and to move the chefs."""

        # To exit 
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        # To move chef1 (upper)
        # Notice we use ifs instead of elif so it can move diagonally!!
        if pyxel.btn(pyxel.KEY_A):
            self.chef1.move("left", self)
        if pyxel.btn(pyxel.KEY_D):
            self.chef1.move("right", self)
        if pyxel.btn(pyxel.KEY_W):
            self.chef1.move("up", self)
        if pyxel.btn(pyxel.KEY_S):
            self.chef1.move("down", self)

        # btnp so it detects just 1 press
        if pyxel.btnp(pyxel.KEY_RSHIFT):
            self.chef1.act()

        # To move chef2 (lower)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.chef2.move("left", self)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef2.move("right", self)
        if pyxel.btn(pyxel.KEY_UP):
            self.chef2.move("up", self)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.chef2.move("down", self)

        if pyxel.btnp(pyxel.KEY_LSHIFT):
            self.chef2.act()

    def draw(self):
        """Pyxel method that also gets executed in every iteration of
        the game (30fps). This is dedicated to draw everything needed on screen.
        """
        # Erasing previous frame
        pyxel.cls(0)

        # For knowing what are the coordinates of every element in the kitchen_map
        # Iterate through the 11 map rows.
        # row represents the vertical position in the map.
        for row in range(len(self.kitchen_map)):
            # Iterate through the 12 characters in this row.
            # column represents the horizontal position.
            for column in range(len(self.kitchen_map[row])):
                pos = self.kitchen_map[row][column]  # Character at this map position

                x = column * self.tiles  # Convert column to screen x-coordinate.
                y = row * self.tiles + self.service_h  # Convert row to screen y-coordinate.
                pyxel.blt(x, y, *self.__scenery_images[pos])  # Draw the matching tile.

        # Drawing the chef. Parameters of pyxel.blt are (x, y, sprite_tuple)
        # * used to unpack the sprite tuple
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.image)

        # if self.chef1.acting:

        # Drawing the second chef
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.image)

        # if self.chef2.acting:

        # A text to show the position of the chef, parameters of
        # pyxel.text are (x, y, text, color)
        # pyxel.text(10, 1, f"({self.chef1.x}, {self.chef1.y})", 7)
        # pyxel.text(10, 10, f"({self.chef2.x}, {self.chef2.y})", 7)

        # Drawing ingredients 
        # y = 20
        # x = 30
        # for ingredient in self.ingredients:
        #     pyxel.blt(x, y, *ingredient.image)
        #     x += 20

      