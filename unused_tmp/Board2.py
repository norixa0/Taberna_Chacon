#!/usr/bin/env python3

# © 2026 norixa0, albertochamaquito8-create. All rights reserved.

import pyxel
from objects.Chef import Chef
from objects.Ingredient import Ingredient


class Board:
    """This class contains a simple board"""
    def __init__(self, width: int, height: int,kitchen_map:list,tiles:int,service_h:int):
        """ Method that creates the board.
        :param width: The width of the board
        :param height: The height of the board
        """
        # Setting the attributes
        self.width = width
        self.height = height
        self.kitchen_map = kitchen_map
        self.tiles=tiles
        self.service_h=service_h

        # The board will contain two Chefs
        self.chef1 = Chef(self.width // 4, self.height // 4, "upper")
        self.chef2 = Chef(self.width * 3 // 4, self.height * 3 // 4, "lower")
        # The board will contain a list of ingredients
        NAMES = ('chorizo', 'potato', 'onion', 'tomato', 'eggs')
        self.ingredients = []
        for ingredient in NAMES:
            ingr = Ingredient(ingredient)
            self.ingredients.append(ingr)
        # In this init we also need to initialize pyxel
        # This instruction is used to initialize pyxel, see API for more
        # parameters
        pyxel.init(self.width, self.height, title="Pyxel game demo",
                   display_scale=4)
        # Loading the pyxres file with the images
        pyxel.load("assets/resources.pyxres")
        # Running the game, this will call the update and draw methods in every
        # frame, see API for more
        pyxel.run(self.update, self.draw)

    # Properties and setters
    @property
    def kitchen_map(self)->list:
        return self.__kitchen_map

    @property
    def tiles(self)->int:
            return self.__tiles
    @property
    def service_h(self)->int:
            return self.__service_h
    
    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @width.setter
    def width(self, width: int):
        if not isinstance(width, int):
            raise TypeError("The width must be an integer")
        if width==192:
            self.__width = width
        else:
            raise ValueError("The width must be 192")

    @height.setter
    def height(self, height: int):
        if not isinstance(height, int):
            raise TypeError("The height must be an integer")
        if height==176:
            self.__height = height
        else:
           raise ValueError("The height must be 176")
    @kitchen_map.setter 
    def kitchen_map(self,kitchen_map:list):
        if not isinstance(kitchen_map,list):
            raise TypeError("kitchen_map must  be a list ")
        if kitchen_map==[
            "CCCCCCCCCCCC",
            "FFFFFFFFFFFF",
            "FFFFFFFFFFFF",
            "FFFFFFFFFFFF",
            "WPWPWBWPWWPW",
            "FFFFFFFFFFFF",
            "FFFFFFFFFFFF",
            "FFFFFFFFFFFF",
            "CCCCCCCCCCCC"]:
            self.__kitchen_map=kitchen_map
        else:
            raise ValueError("The kitchen map must be"
                              "CCCCCCCCCCCC",
                              "FFFFFFFFFFFF",
                              "FFFFFFFFFFFF",
                              "FFFFFFFFFFFF",
                              "WPWPWBWPWWPW",
                              "FFFFFFFFFFFF",
                              "FFFFFFFFFFFF",
                              "FFFFFFFFFFFF",
                              "CCCCCCCCCCCC")
    @tiles.setter
    def tiles(self,tiles:int):
        if not isinstance(tiles,int):
            raise TypeError("tiles must be an integer")
        if tiles==16:
            self.__tiles=tiles
        else :
            raise ValueError("tiles dimension must be 16")
    @service_h.setter
    def service_h(self,service_h:int):
        if not isinstance(service_h,int):
            raise TypeError("service_h must be an integer")
        if service_h==32:
            self.__service_h=service_h
        else:
            raise ValueError("service_h value must be 32 ")
    def update(self):
        """ This is the pyxel method that gets executed in every iteration of
        the game (every frame). You need to put here all the code that has to
        be executed in every frame. Now it contains the logic to exit the
        program if Q key is pressed and to move the chefs."""
        # To exit the game
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        # To move the chef1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.chef1.move("left", self)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.chef1.move("right", self)
        if pyxel.btn(pyxel.KEY_UP):
            self.chef1.move("up", self)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.chef1.move("down", self)
        # We use btnp so it detects just 1 press
        if pyxel.btnp(pyxel.KEY_RSHIFT):
            self.chef1.act()
        # To move the chef2, if we use elif it cannot move in diagonal
        if pyxel.btn(pyxel.KEY_A):
            self.chef2.move("left", self)
        elif pyxel.btn(pyxel.KEY_D):
            self.chef2.move("right", self)
        elif pyxel.btn(pyxel.KEY_W):
            self.chef2.move("up", self)
        elif pyxel.btn(pyxel.KEY_S):
            self.chef2.move("down", self)
        # We use btnp so it detects just 1 press
        elif pyxel.btnp(pyxel.KEY_LSHIFT):
            self.chef2.act()

    def draw(self):
        """This is the pyxel method that gets executed in every iteration of
        the game (every frame). You need to put here all the code to draw the
        sprites of the game.
        """
        # Erasing the previous screen
        pyxel.cls(0)
        # Drawing the chef. Parameters of pyxel.blt are (x, y, sprite_tuple)
        # The * is used to unpack the sprite tuple
        pyxel.blt(self.chef1.x, self.chef1.y, *self.chef1.image)
        # If the chef is acting we draw a text above it
        if self.chef1.acting:
            pyxel.text(self.chef1.x, self.chef1.y - 5, 'Action', 2)
        # Drawing the second chef
        pyxel.blt(self.chef2.x, self.chef2.y, *self.chef2.image)
        if self.chef2.acting:
            pyxel.text(self.chef2.x, self.chef2.y - 5, 'Action', 2)
        # A text to show the position of the chef, parameters of
        # pyxel.text are (x, y, text, color)
        pyxel.text(10, 1, f"({self.chef1.x}, {self.chef1.y})", 7)
        pyxel.text(10, 10, f"({self.chef2.x}, {self.chef2.y})", 7)
        # Drawing ingredients
        y = 20
        x = 30
        for ingredient in self.ingredients:
            pyxel.blt(x, y, *ingredient.image)
            x += 20
