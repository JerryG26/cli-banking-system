from account import Account
from exception.invalid_amount_exception import InvalidAmountException

class CheckingAccount(Account):

    def __init__(self,balance:float):
        super().__init__(balance)

    def deposit(self,money:float)->None:
        if money > 0:
            total = self._balance + money
            self._balance = total
            print("Transaction Succesful.")
        else:
            raise InvalidAmountException()
    
    def withdraw(self,money)->None:
        if money > 0:
            total = self._balance - money
            self._balance = total
            print("Transaction Succesful.")
        else:
            raise InvalidAmountException()

    def transfer_money(self,user_account:Account,money:float)->bool:
        if not user_account:
            print("User is invalid")
            return False
        
        if money > 0:
            total = user_account._balance + money
            user_account._balance = total
            print("Transaction Succesfull.")
        else:
            raise InvalidAmountException()

        return True