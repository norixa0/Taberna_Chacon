class Station :
    def __init__(self,col:int,row:int,kind:str,content:object):
        self.col=col
        self.row=row
        self.kind=kind 
        self.content=content

    @property
    def col(self)->int:
        return self.__col
    @col.setter 
    def col(self,col:int):
        if not isinstance(col,int):
            raise TypeError("Col must be an integer")
        if col<0:
            raise ValueError("Col must be a positive number")
        else:
            self.__col=col
    @property
    def row(self)->int:
        return self.__row 
    @row.setter
    def row(self,row:int):
        if not isinstance(row,int):
            raise TypeError("Row must be an integer")
        if row <0:
            raise ValueError("Row must be a positive integer")
        else:
            self.__row=row
    @property
    def kind(self)->str:
        return self.__kind
    @kind.setter
    def kind(self,kind:str):
        if not isinstance(kind,str):
            raise TypeError("Kind must be a string")
        self.__kind = kind
    @property
    def content(self)->object:
        return self.__content 
    @content.setter
    def content(self,content:object):
        if not isinstance(content,object):
            raise TypeError("Content must be an object")
        self.__content = content
        

        
        
        
        

