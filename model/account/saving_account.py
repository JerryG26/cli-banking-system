from account import Account
from datetime import datetime
from exception.invalid_amount_exception import InvalidAmountException

#make the interest work 

class SavingAccount(Account):
    __INTEREST = 0.02

    def __init__(self,balance:float):
        super().__init__(balance)
        self.__last_interest_date = datetime.now()

        
    def deposit(self,money:float)->None:
        if money <= 0:
            raise InvalidAmountException()

        self._balance += money
        print("Transaction Succesful.")
    
    def withdraw(self,money)->None:
        if money <= 0 or money > self._balance:
            raise InvalidAmountException()

        self._balance -= money
        print("Transaction Succesful.")
            
    def transfer_money(self,user_account:Account,money:float)->bool:
        if not user_account:
            print("User is invalid")
            return False
        
        if money <= 0 or money > self._balance:
            raise InvalidAmountException()

        user_account._balance += money
        self._balance -= money
        print("Transaction Succesfull.")

        return True

    @property
    def last_interest_date(self)->datetime:
        return self.__last_interest_date

    @last_interest_date.setter
    def last_interest_date(self,current_date:datetime)->None:
        self.__last_interest_date = current_date
            
    def __increase_balance(self):
        self._balance += (self.__INTEREST / 12.00) * self._balance

#incomplete task: checking the date to apply the interest.

