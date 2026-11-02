from account import Account
from datetime import datetime
from exception.invalid_amount_exception import InvalidAmountException


class SavingAccount(Account):
    __INTEREST = 0.02

    def __init__(self,balance:float,date:datetime):
        super().__init__(balance)
        self.__last_interest_date = date
        
    @property
    def last_interest_date(self)->datetime:
        return self.__last_interest_date

    def pay(self,money):
        if money > self._balance:
            raise InvalidAmountException()

        self._balance -= money

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
            
    def transfer_money(self,user_account:Account,money:float)->None:
        if not user_account:
            print("User is invalid")
            return 
        
        if money <= 0 or money > self._balance:
            raise InvalidAmountException()

        user_account._balance += money
        self._balance -= money
        print("Transaction Succesfull.")

#Function to check the month to apply the interest and increase the balance
    @last_interest_date.setter
    def last_interest_date(self,current_date:datetime)->None:
        if self.__last_interest_date != current_date:
            self.__increase_balance()
            self.__last_interest_date = current_date

    def __increase_balance(self):
        self._balance += (self.__INTEREST / 12.00) * self._balance



