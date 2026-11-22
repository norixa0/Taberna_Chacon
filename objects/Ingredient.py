class Ingredient:
    """ This class contains a simple ingredient. It has a name and an image.
    The image is a read only attribute that depends on the name. In the
    future the image will depend also on the state of the ingredient: chopped,
    cooked, etc. """
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        NAMES = ('chorizo', 'potato', 'onion', 'tomato', 'eggs')
        if not isinstance(value, str):
            raise TypeError("The name of the ingredient must be a str")
        elif value.lower() not in NAMES:
            raise ValueError("The valid names are " + str(NAMES))
        else:
            self.__name = value.lower()

    @property
    def image(self) -> tuple:
        # We use a dictionary to map the name of the ingredient to its image.
        IMAGES_RAW = {
            "chorizo": (0, 48, 16, 16, 16),
            "potato": (0, 16, 16, 16, 16),
            "onion": (0, 32, 16, 16, 16),
            "tomato": (0, 0, 16, 16, 16),
            "eggs": (0, 64, 16, 16, 16),
        }
        return IMAGES_RAW[self.name]
