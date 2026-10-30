class User:

    def __init__(self,name:str,password):
        self.__name = name
        self.__password = password

    @property
    def name(self)->str:
        return self.__name

    @property
    def password(self)->str:
        return self.__password

    @name.setter
    def name(self,name:str)->None:
        self.__name = name

    @password.setter
    def password(self,password:str)->None:
        self.__password = password

    def __name__(self)->str:
        return "User class"