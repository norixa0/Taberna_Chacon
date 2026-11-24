class Recipe :
    def __init__(self,name:str,ingredients:list,equipment:str):
        self.name = name 
        self.ingredients = ingredients
        self.equipment=equipment
    @property
    def name(self)->str:
        return self.__name
    @name.setter
    def name(self,name:str):
        if not isinstance(name,str):
            raise TypeError("name must be a string")
        self.__name=name

    @property
    def ingredients(self)->list:
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self,ingredients:list):
        if not isinstance(ingredients,list):
            raise TypeError("Ingredients must be a list")
        for i in ingredients:
            if not isinstance(i, str):
                raise TypeError("Every ingredient must be a string")
        self.__ingredients=ingredients
        
    @property
    def equipment(self)->str:
        return self.__equipment
    
    @equipment.setter
    def equipment(self,equipment:str):
        if not isinstance(equipment,str):
            raise TypeError("Equipment must be a string")
        self.__equipment=equipment
        