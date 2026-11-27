class Dish :
    def __init__(self):
        self.ingredients=[]
    @property 
    def ingredients(self)->list:
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self,ingredients:list):
        if not isinstance(ingredients,list):
            raise TypeError("ingredients must be a list")
        self.__ingredients = ingredients


    def is_empty(self):    #Checks if the list is empty 
        empty=False
        if len(self.ingredients)==0:
            empty=True
            print("The list is empty")
        else:
            print("The list is not empty")
            
        return empty 

    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


    

