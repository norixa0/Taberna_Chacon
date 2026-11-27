
#!/usr/bin/env python3

# © 2026 norixa0, albertochamaquito8-create. All rights reserved.

import json
import pyxel
from objects.Chef import Chef
from objects.Ingredient import Ingredient

class Board:
    def __init__(self):
        """ Method that creates the board. 
        Additional parameters can be modified through assets/config.json
        """
        with open("objects/assets/config.json", "r") as file: # Read config.json
            self.__config_data = json.load(file)
        with open("objects/assets/resources.json", "r") as file: 
            self.__resources = json.load(file)

        # Define parameters (obtains them from json file)
        self.__screen_title = self.__config_data["SCREEN_TITLE"] # Title for the root window
        self.__width = self.__config_data["SCREEN_W"] # Screen width
        self.__height = self.__config_data["SCREEN_H"] # Screen height
        self.__kitchen_map = self.__config_data["KITCHEN_MAP"] # Kitchen map (9 rows, 12 columns)
        self.__tiles_size = self.__config_data["TILES_SIZE"] # Tile size in pixels (16x16 default)
        self.__bg_color_sprites = self.__config_data["BG_COLOR_SPRITES"] # Self explanatory
        self.__controls = self.__config_data["CHEF_DIRECTIONS"]["controls"] # Controls for each chef
        # These cannot be in the json file, because json stores them as strings, and we need the pyxel.KEY_ constants.
        self.__pyxel_keys = {
            "KEY_A": pyxel.KEY_A,
            "KEY_D": pyxel.KEY_D,
            "KEY_W": pyxel.KEY_W,
            "KEY_S": pyxel.KEY_S,
            "KEY_LEFT": pyxel.KEY_LEFT,
            "KEY_RIGHT": pyxel.KEY_RIGHT,
            "KEY_UP": pyxel.KEY_UP,
            "KEY_DOWN": pyxel.KEY_DOWN,
            "KEY_RSHIFT": pyxel.KEY_RSHIFT,
            "KEY_LSHIFT": pyxel.KEY_LSHIFT,
        }

        # Image parameters to draw later:
        # The lists in json file is in format: [bank, row, column, width, height]
        self.__scenery_images = self.__resources["SCENERY_IMAGES"] # Scenery images in format. 
        self.__chef_images = self.__resources["CHEF_IMAGES"] # Chef images in format.

        # The board contains two Chefs
        self.__chef1 = Chef(self.width // 4, self.height // 3, "upper")
        self.__chef2 = Chef(self.width * 3 // 4, self.height * 3 // 4, "lower")

        # List of ingredients, assign them an object and append them to self.ingredients.
        NAMES = ('chorizo', 'potato', 'onion', 'tomato', 'eggs')
        self.ingredients = []
        for ingredient in NAMES:
            ingr = Ingredient(ingredient)
            self.ingredients.append(ingr)

        # Initialize pyxel
        pyxel.init(self.width, self.height, title=self.screen_title, display_scale=4)
        # Loading the pyxres file with the images
        pyxel.load("assets/resources.pyxres")
        # Running the game, this will call the update and draw methods every frame (30fps)
        pyxel.run(self.update, self.draw)

    # ---- PROPERTIES ----
    @property
    def screen_title(self) -> int:
        return self.__screen_title
    
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
    def tiles_size(self) -> int:
        return self.__tiles_size

    @property
    def bg_color_sprites(self) -> int:
        return self.__bg_color_sprites

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

        # Check each direction independently so chefs can move diagonally.
        for chef in (self.__chef1, self.__chef2):
            chef_controls = self.__controls[chef.location]
            horizontal_direction = None
            vertical_direction = None
            # Check if the movement keys are pressed for each chef
            for direction, key_name in chef_controls["movement"].items():
                if pyxel.btn(self.__pyxel_keys[key_name]):
                    chef.move(direction, self) # Move the chef in the direction if the key is pressed
                    # If both horizontal and vertical directions are pressed, we will combine them to make a diagonal movement.
                    if direction == "left" or direction == "right":
                        horizontal_direction = direction
                    elif direction == "up" or direction == "down":
                        vertical_direction = direction

            # Override previous direction if both horizontal and vertical directions are pressed, to make a diagonal movement.
            if horizontal_direction is not None and vertical_direction is not None:
                chef.direction = horizontal_direction + "-" + vertical_direction

            # btnp detects just one press. Action key is pressed, we will call the act method of the chef.
            if pyxel.btnp(self.__pyxel_keys[chef_controls["action"]]):
                chef.act() # activate the action of the chef (change the acting attribute to True or False, depending on its previous state)

        self.__frame_count += 1  
        if self.__frame_count == 30: #this is the loop used for making the counter 
            self.__timer = self.__timer + 1 #we add 1 second for every 30 iterations that the program has done 
            self.__frame_count = 0 # Resets the frame counter to start counting the next second

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

                x = column * self.tiles_size  # Convert column to screen x-coordinate.
                y = row * self.tiles_size # Convert row to screen y-coordinate.
                pyxel.blt(x, y, *self.scenery_images[pos], colkey=self.bg_color_sprites)  # Draw the matching tile.

        pyxel.text(125,5, "Time: " + str(self.__timer), 9)
        # Drawing the chef. Parameters of pyxel.blt are (x, y, sprite_tuple)

        pyxel.text(125,13,"Score: " + str(self.__score), 8)
 
        pyxel.text(125,21,"Failures: " + str(self.__failures) , 3)

        pyxel.text(13 , 13  ,"Orders: " + str(self.__orders), 10)
        
       # pyxel.text()
        # * used to unpack the sprite tuple
        pyxel.blt(self.__chef1.x, self.__chef1.y, *self.__chef1.image, colkey=self.bg_color_sprites)

        # Drawing the second chef
        pyxel.blt(self.__chef2.x, self.__chef2.y, *self.__chef2.image, colkey=self.bg_color_sprites)

        # A text to show the position of the chef, parameters of
        # pyxel.text are (x, y, text, color)
        # pyxel.text(10, 1, f"({self.__chef1.x}, {self.__chef1.y})", 7)
        # pyxel.text(10, 10, f"({self.__chef2.x}, {self.__chef2.y})", 7)

        # Drawing ingredients 
        # y = 20
        # x = 30
        # for ingredient in self.ingredients:
        #     pyxel.blt(x, y, *ingredient.image)
        #     x += 20

      