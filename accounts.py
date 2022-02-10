# A class to management the accounts and operations around there
class Account:
    def __init__(self, clients, number,balance=0):
        self.balance=0
        self.clients=clients
        self.number=number
        self.operations=[]
        self.contact = self.clients[0], self.number
        self.deposit(balance)


    def abstract(self):
        print("CA Number: %s - Balance: %5.2f - %s Phone number: %s" %(self.number,self.balance,self.clients[0],self.clients[1]))

    def withdraw(self, value):
        if self.balance>=value:
            self.balance-=value
            #print(self.balance)
            self.operations.append(["WITHDRAW",value])
        else:
            print("No enough cash, try another value!")
            #print(self.clients,self.balance)

    def deposit(self,value):
        self.balance+=value
        self.operations.append(["DEPOSIT", value])
        #print(self.clients,self.balance)

    def extract(self):
        print("Extract CA num %s\n"%self.number)
        for o in self.operations:
            print("%10s %10.2f\n"%(o[0],o[1]))
        print("\n    Balance: %10.2f\n"%self.balance)

# This is a different account, it's special. Special accounts have a extra negative limit.
# In this it was necessary inherit previous class and use their objects
class SpecialAccount(Account):
    def __init__(self, clients,number,balance=0,limit=0):
        Account.__init__(self,clients,number,balance)
        self.limit=limit

    def withdraw(self, value):
        if self.balance+self.limit>=value:
            self.balance-=value
            self.operations.append(["Withdraw",value])
        else:
            self.operations.append(["Withdraw Error!\nYou don't have limit enough!",value])

