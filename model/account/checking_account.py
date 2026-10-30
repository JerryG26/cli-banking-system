from account import Account
from exception.invalid_amount_exception import InvalidAmountException

#Update checking account behavior
class CheckingAccount(Account):

    def __init__(self,balance:float):
        super().__init__(balance)

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

#Fixed major problems. 
#Lacking specifi behavior