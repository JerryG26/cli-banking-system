from user import User
from datetime import datetime
from account.checking_account import CheckingAccount
from account.saving_account import SavingAccount
class Customer(User):

    def __init__(self,name:str,password:str,saving_account:SavingAccount,checking_account:CheckingAccount):
        super().__init__(name,password)
        self.__address = ""
        self.__age = 18
        self.__brithday = ""
        self.__saving_account = saving_account
        self.__checking_account = checking_account
        self.__date_created = datetime.now()

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
    def saving_account(self)->SavingAccount | None:
        return self.__saving_account
    
    @property
    def checking_account(self)->CheckingAccount | None:
        return self.__checking_account

    @property
    def date_created(self)->datetime:
        return self.__date_created
    
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
    def saving_account(self,saving_account:SavingAccount)->None:
        self.__saving_account = saving_account

    @checking_account.setter
    def checking_account(self,checking_account:CheckingAccount)->None:
        self.__checking_account = checking_account

    def set_current_date(self,current_date:datetime)->None:
        self.__saving_account.last_interest_date = current_date

    def __str__(self)->str:
        return "Customer Class"