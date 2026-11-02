from abc import ABC,abstractmethod
from exception.invalid_amount_exception import InvalidAmountException
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

    @abstractmethod
    def deposit(self,money:float)->None:
        pass

    @abstractmethod
    def withdraw(self,money)->None:
        pass

    @abstractmethod  
    def transfer_money(self,user_account:Account,money:float)->None:
        pass

    @abstractmethod
    def pay(self,money)->None:
        pass

    def __str__(self)->str:
        return "Account Class"
