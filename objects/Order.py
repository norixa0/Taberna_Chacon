class Order:
    def __init__(self,recipe:str,time_left:int):
        self.recipe = recipe 
        self.time_left=time_left
    @property
    def recipe(self)->str:
        return self.__recipe
    @recipe.setter
    def recipe(self,recipe:str):
        if not isinstance(recipe,str):
            raise TypeError("Recipe must be a string")
        self.__recipe=recipe
    @property
    def time_left(self)->int:
        return self.__time_left
    @time_left.setter
    def time_left(self,time_left:int):
        if not isinstance(time_left,int):
            raise TypeError("Time left must be an integer")

    def update(self):
        self.time_left = self.time_left - 1