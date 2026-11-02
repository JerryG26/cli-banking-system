from account import Account
from exception.invalid_amount_exception import InvalidAmountException

#Update checking account behavior
class CheckingAccount(Account):

    def __init__(self,balance:float):
        super().__init__(balance)
        self.__isActive = "pending"
        self.__overdraft_limit = 0.00
        self.__pending_payment = 0.00

    def pay(self,money)->None:

        if self.__isActive == "active" and money > self._balance and self.__overdraft_limit > money:
            self.over_draft(money)

        if self.__isActive != "active" or money > self._balance:
            raise InvalidAmountException()

        self._balance -= money

    def deposit(self,money:float)->None:
        if money <= 0:
            raise InvalidAmountException()
        
        self._balance += (money - self.__pending_payment)
        if self.__pending_payment > money:
            self.__pending_payment -= money
        else:
            self.__pending_payment = 0

        print("Transaction Succesful.")

    def withdraw(self,money)->None:

        if self.__isActive == "active" and money > self._balance and self.__overdraft_limit > money:
            self.over_draft(money)

        if money <= 0 or money > self._balance:
            raise InvalidAmountException()

        self._balance -= money
        print("Transaction Succesful.")
            
    def transfer_money(self,user_account:Account,money:float)->None:
        if not user_account:
            print("User is invalid")
            return 

        if self.__isActive == "active" and money > self._balance and self.__overdraft_limit > money:
            self.over_draft(money)

        if money <= 0 or money > self._balance:
            raise InvalidAmountException()
        
        user_account._balance += money
        self._balance -= money
        print("Transaction Succesfull.")

    def over_draft(self,money:float)->None:
        self.__pending_payment += (money - self._balance)

           