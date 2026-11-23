#fernan and daniel 2026 

from objects.Board import Board

class Chef:
    """ A improved version of the Chef class for the final project. It
    contains properties, setters, a move method and an act method. The sprite
    of the chef is a read only attribute that depends on its position, which
    is a private attribute. """
    def __init__(self, x: int, y: int, pos: str):
        """ Init method of the class
        :param x: the x of the chef
        :param y: the y of the chef
        :param pos: the position of the chef: ("upper", "lower")
        """
        self.x = x
        self.y = y
        # At the beginning it has no dish and is not acting
        self.has_dish = False
        self.acting = False
        # The sprite will be a read only attribute that depends on the
        # POSITION, which will be a private one.
        POSITIONS = ("upper", "lower")
        if not isinstance(pos, str):
            raise TypeError("The position of the Chef must be a str")
        elif pos.lower() not in POSITIONS:
            raise ValueError("The valid positions are " + str(POSITIONS))
        else:
            # We create it as private constant as Chefs will never change area
            self.__POSITION = pos.lower()

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def image(self) -> tuple:
        """ The image will be a read only attribute, that will depend initially
         on the POSITION. In Pyxel the image is a tuple with the coordinates of
         the image in the image bank.The tuple is (image_bank, starting_x,
         starting_y, horizontal_size, vertical_size)
        """
        if self.__POSITION == "upper":
            result = (0, 0, 0, 16, 16)
        else:
            result = (0, 0, 112, 16, 16)
        return result

    @property
    def has_dish(self) -> bool:
        return self.__has_dish

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("The x position must be an int")
        elif x < 0:
            raise ValueError("The x cannot be negative")
        else:
            self.__x = x

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("The y position must be an int")
        elif y < 0:
            raise ValueError("The y cannot be negative")
        else:
            self.__y = y

    @has_dish.setter
    def has_dish(self, dish: bool):
        if not isinstance(dish, bool):
            raise TypeError("The has_dish attribute must be bool")
        else:
            self.__has_dish = dish

    # Notice we cannot put the type of board to be Board as that would require
    # importing Board and we will have a circular import, so we indicate the
    # type using "Board"
    def move(self, direction: str, board: "Board"):
        """
        This is an example of how to move the chef. No obstacles in the board
        are considered.
        :param direction: a string which can be 'left' or 'right'
        :param board: the Board, we could have received its vertical and
         horizontal sizes, but as in the future, to move we need to consider
         other board components it is better to receive the whole board as
         parameter
        """
        DIRECTIONS = ("left", "right", "up", "down")
        board_x_size = board.width
        board_y_size = board.height
        # Checking the type and value of the parameters, we cannot check the
        # type of board as it is a circular import
        if not isinstance(direction, str):
            raise TypeError("The direction must be a string")
        elif direction.lower() not in DIRECTIONS:
            raise ValueError("The direction must be in " + str(DIRECTIONS))
        # We convert the direction to lower case to avoid problems with upper
        # case letters
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
