#!/usr/bin/env python3

# © 2026 norixa0, albertochamaquito8-create. All rights reserved.

import json

class Chef:
    def __init__(self, x: int, y: int, location: str):
        """:param x: the x of the chef
        :param y: the y of the chef
        :param location: the location of the chef (must be in CHEF_POSITIONS)
        """
        with open("objects/assets/config.json", "r") as file: # Read config.json
           self.__config_data = json.load(file)
        with open("objects/assets/resources.json", "r") as file: 
            self.__resources = json.load(file)


        self.__chef_positions = tuple(self.__config_data["CHEF_POSITIONS"])
        self.__chef_directions = tuple(self.__config_data["CHEF_DIRECTIONS"]["valid"])

        # Assign attributes
        self.x = x
        self.y = y
        self.location = location
        self.direction = "up" # Default direction is down, but it will change when the chef moves

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
    def location(self) -> str:
        return self.__location

    @property
    def direction(self) -> str:
        return self.__direction
    
    @property
    def image(self) -> tuple:
        """Image is a read only attribute, that will depend initially
        on the POSITION. The image is a tuple with the coordinates of
        the image in the image bank. (image_bank, starting_x,
        starting_y, horizontal_size, vertical_size)
        """
        if self.__location in self.__resources["CHEF_IMAGES"]:
            return tuple(self.__resources["CHEF_IMAGES"][self.__location][self.__direction])

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

    @location.setter
    def location(self, location: str):
        if not isinstance(location, str):
            raise TypeError("The position of the Chef must be a str")
        if location.lower() not in self.__chef_positions:
            raise ValueError("The valid positions are " + str(self.__chef_positions))
        # We create it as private constant as Chefs will never change area
        self.__location = location.lower()

    @direction.setter
    def direction(self, direction: str):
        if not isinstance(direction, str):
            raise TypeError("The direction must be a string")
        if direction.lower() not in self.__chef_directions:
            raise ValueError("The valid directions are " + str(self.__chef_directions))
        self.__direction = direction.lower()

    @has_dish.setter
    def has_dish(self, dish: bool):
        if not isinstance(dish, bool):
            raise TypeError("The 'has_dish' attribute must be a bool")
        self.__has_dish = dish

    @acting.setter
    def acting(self, acting: bool):
        if not isinstance(acting, bool):
            raise TypeError("The 'acting' attribute must be a bool")
        self.__acting = acting


    # ---- METHODS ---- 
    # indicate "Board" with "" so the program doesn't crash for not importing Board (would give problems)
    def move(self, direction: str, board: "Board"):
        """ Moving the chef
        :param direction: a string containing the direction to move
        :param board: the Board object, to check the size of the board and avoid moving out of it
        """

        board_x_size = board.width
        board_y_size = board.height

        # If direction is not valid, it will raise an error in the setter of direction
        self.direction = direction.lower() # Change the direction of the chef to the new one (for sprite animation)
        # We can move the chef to the right if its x + size is < width
        if direction == "right" and self.x + self.image[3] < board_x_size:
            self.x += 1
        # We can move the chef to the left if its x-coordinate is > 0
        elif direction == "left" and self.x > 0:
            self.x -= 1
        # We can move it up if its y > 0
        elif direction == 'up' and self.y > 0:
            if self.__location == "lower" and self.y - 1 > 14 + (board_y_size // 2):
                self.y -= 1
            elif self.__location == "upper" and self.y - 1 > 36:
                self.y -= 1
        # Finally, it can be moved down if its y + size is < height
        elif direction == "down" and self.y + self.image[4] < board_y_size:
            if self.__location == "lower" and self.y + 1 < board_y_size - 32:
                self.y += 1
            elif self.__location == "upper" and self.y + 1 < (board_y_size // 2) - 8:
                self.y += 1

    def act(self):
        """ This method changes the state of the acting attribute"""
        self.acting = not self.acting
