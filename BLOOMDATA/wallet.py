class Wallet: 
    def __init__(self,initial_amount=0):
        #save the user provided initial amount as an attribute
        self.balance = initial_amount

    def spend_cash(self,amount):
        if self.balance < amount:
            return "Not enough money"
        else: 
            self.balance = self.balance - amount
            return f"remaining balance: {self.balance}"

    #__repr__ method
    #changes how the object looks when it is printed out
    # the presence of the self keyword allows me to access or
    # modify class attributes within this function 
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"
    
    def add_cash(self,amount):
        self.balance = self.balance + amount
        return f"New balance of: {self.balance}"


if __name__ == "__main__":
    wallet1 = Wallet(100)
    wallet2 = Wallet(200)
    wallet3 = Wallet(3000)
    # print(wallet1.balance)
    print(wallet1.spend_cash(120))
    # print(wallet1.spend_cash(60))
    # print(wallet1.balance)
    # print(wallet1.add_cash(180))
    # print(wallet1.balance)
    # print(wallet1.spend_cash(120))
    print(wallet1,wallet2,wallet3)
    #self is self contained and does not effect the other wallet variables

