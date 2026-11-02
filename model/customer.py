from user import User
from datetime import datetime
from account.account import Account
from account.checking_account import CheckingAccount
from account.saving_account import SavingAccount
from exception.invalid_amount_exception import InvalidAmountException
class Customer(User):

    def __init__(self,name:str,password:str,saving_account:Account):
        super().__init__(name,password)
        self.__address = ""
        self.__age = 18
        self.__brithday = ""
        self.__account = saving_account
        self.__date_created = datetime.now()

    def deposit(self,money)->bool:
        try:
            self.__account.deposit(money)
        except InvalidAmountException as e:
            print(e)
            return False
        return True
    
    def withdraw(self,money)->bool:
        try:
            self.__account.withdraw(money)
        except InvalidAmountException as e:
            print(e)
            return False
        return True

    def pay(self,money)->bool:
        try:
            self.__account.pay(money)
        except InvalidAmountException as e:
            print(e)
            return False
        return True

    def transfer(self,account:Account,money:float)->bool:
        try:
            self.__account.transfer_money(account,money)
        except InvalidAmountException as e:
            print(e)
            return False
        return True

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

    #Special function for SavingAccount to set the current time for interest
    def set_current_date(self,current_date:datetime)->None:
        if isinstance(self.__account,SavingAccount):
            self.__account.last_interest_date = current_date

    def __str__(self)->str:
        return "Customer Class"