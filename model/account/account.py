from abc import ABC,abstractmethod

class Account(ABC):

    def __init__(self,balance:float):
        self.__balance = balance

    @property
    def check_balance(self)->float:
        return self.__balance

    @property
    def _balance(self)->float:
        return self.__balance

    @_balance.setter
    def _balance(self,balance)->None:
        self.__balance = balance

    def __str__(self)->str:
        return "Account Class"

    @abstractmethod
    def deposit(self,money)->None:
        pass

    @abstractmethod
    def withdraw(self,moeny)->None:
        pass

    @abstractmethod
    def transfer_money(self,user_account:Account,money:float)->bool:
        pass