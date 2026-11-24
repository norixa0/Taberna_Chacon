#!/usr/bin/env python3

# © 2026 norixa0, albertochamaquito8-create. All rights reserved.

import json,os

class Chef:
    """Chef class for the final project. Contains properties, setters, 
    a move method and an act method."""
    def __init__(self, x: int, y: int, POS: str):
        """:param x: the x of the chef
        :param y: the y of the chef
        :param pos: the position of the chef (must be in CHEF_POSITIONS)
        """
        with open("objects/assets/config.json", "r") as file: # Read config.json
           self.__config_data = json.load(file)

        # Load data into self (using setters and properties)
        self.__CHEF_POSITIONS = self.__config_data["CHEF_POSITIONS"]
        self.x = x
        self.y = y
        # position will be a constant once it's defined (chefs don't change area)
        self.__POS = None
        self.POS = POS

        # At the beginning it has no dish and is not acting
        # Set attribs with properties and setters
        self.has_dish = False
        self.acting = False


    # ---- PROPERTIES ---- 
    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def POS(self) -> str:
        return self.__POS
    
    @property
    def image(self) -> tuple:
        """Image is a read only attribute, that will depend initially
        on the POSITION. The image is a tuple with the coordinates of
        the image in the image bank. (image_bank, starting_x,
        starting_y, horizontal_size, vertical_size)
        """
        if self.__POS == "upper":
            # (bank, column, row, width, height)
            result = (0, 0, 0, 16, 16)
        else: 
            result = (0, 0, 16, 16, 16)
        return result

    @property
    def has_dish(self) -> bool:
        return self.__has_dish

    @property
    def acting(self) -> bool:
        return self.__acting
    

    # ---- SETTERS ----
    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("The x position must be an int")
        if x < 0:
            raise ValueError("The x cannot be negative")
        self.__x = x

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("The y position must be an int")
        if y < 0:
            raise ValueError("The y cannot be negative")
        self.__y = y


    # i have to change this - norixa0
    @POS.setter
    def POS(self, POS: str):
        if self.__POS is not None:
            raise ValueError("Modifying POS attribute is forbidden.")
        if not isinstance(POS, str):
            raise TypeError("The position of the Chef must be a str")
        if POS.lower() not in self.__CHEF_POSITIONS:
            raise ValueError("The valid positions are " + str(self.__CHEF_POSITIONS))
        # We create it as private constant as Chefs will never change area
        self.__POS = POS.lower()

    @has_dish.setter
    def has_dish(self, dish: bool):
        if not isinstance(dish, bool):
            raise TypeError("The 'has_dish' attribute must be a bool")
        self.__has_dish = dish

    @acting.setter
    def acting(self, acting: bool):
        if not isinstance(acting, bool):
            raise TypeError("The 'acting' attribute must be a bool")


    # ---- METHODS ---- 
    # indicate "Board" with "" so the program doesn't crash for not importing Board (would give problems)
    def move(self, direction: str, board: "Board"):
        """ Moving the chef
        :param direction: a string containing the direction to move
        :param board: the Board, we could have received its vertical and
        horizontal sizes, but as in the future, to move we need to consider
        other board components it is better to receive the whole board as
        parameter
        """
        DIRECTIONS = ("left", "right", "up", "down")
        board_x_size = board.width
        board_y_size = board.height
        if not isinstance(direction, str):
            raise TypeError("The direction must be a string")
        elif direction.lower() not in DIRECTIONS:
            raise ValueError("The direction must be in " + str(DIRECTIONS))
        
        # Convert to lower case
        direction = direction.lower()

        # The (0, 0) position of the chef is the top left corner of the
        # sprite. We can move the chef to the right if the rightmost
        # x-coordinate of the chef is less than the board size. It will be
        # the x-coordinate of the chef plus the width of the sprite. The
        # width of the sprite is the 4th element of the image tuple.
        if direction == "right" and self.x + self.image[3] < board_x_size:
            self.x += 1
        # We can move the chef to the left if its x-coordinate is > 0
        elif direction == "left" and self.x > 0:
            self.x -= 1
        # We can move it up if its y > 0
        elif direction == 'up' and self.y > 0:
            self.y -= 1
        # Finally, it can be moved down if its y + size is < height
        elif direction == "down" and self.y + self.image[4] < board_y_size:
            self.y += 1

    def act(self):
        """ This method changes the state of the acting attribute"""
        self.acting = not self.acting
