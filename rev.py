class Bank:
    def __init__(self,create,modify,delete):
        self.create=create
        self.modify=modify
        self.delete=delete

    def createAcc(self,owner) :
        pass
    def modifyAcc(self):
        pass
    def deleteAcc(self):
        pass   


class BankAccount(Bank):
    balance= 0

    def __init__(self,deposit,withdraw,balance):
        self.deposit=deposit
        self.withdraw=withdraw
        self.balance= balance

    def depositMoney(self):
        pass
    def withdrawMoney(self):
        pass
    def checkBalance(self):
        pass
       


