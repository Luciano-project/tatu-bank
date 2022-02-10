# This class create the object to start the aplication
class Client:
    def __init__(self,name,numb):
        self.name=name
        self.numb=numb

# In this part we'll register data and after create a client account
class ClientRegister:
    def __init__(self):
        self.name=input("Complete name: ")
        self.numb=input("Cell Phone number: ")



