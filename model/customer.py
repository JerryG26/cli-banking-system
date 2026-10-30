from user import User
from account.account import Account
class Customer(User):

    def __init__(self,name:str,password:str,saving_account:Account,checking_account:Account):
        super().__init__(name,password)
        self.__address = ""
        self.__age = 18
        self.__brithday = ""
        self.__saving_account = saving_account
        self.__checking_account = checking_account

    @property
    def address(self)->str:
        return self.__address   

    @property
    def age(self)->int:
        return self.__age

    @property
    def birthday(self)->str:
        return self.__brithday

    @property
    def saving_account(self)->Account | None:
        return self.__saving_account
    
    @property
    def checking_account(self)->Account | None:
        return self.__checking_account

    @address.setter
    def address(self,address)->None:
        self.__address = address

    @age.setter
    def age(self,age)->None:
        self.__age = age

    @birthday.setter
    def birthday(self,birthday)->None:
        self.__brithday = birthday

    @saving_account.setter
    def saving_account(self,saving_account:Account)->None:
        self.__saving_account = saving_account

    @checking_account.setter
    def checking_account(self,checking_account:Account)->None:
        self.__checking_account = checking_account

    def __str__(self)->str:
        return "Customer Class"