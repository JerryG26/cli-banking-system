class InvalidAmountException(Exception):
    def __init__(self):
        super().__init__("Amount is not valid.")