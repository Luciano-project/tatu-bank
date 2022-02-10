# Here we'll test the aplication. This is the main of operation, all objects get connected here.

#import all the modules and objects
from clients import Client,ClientRegister
from banks import Bank
from accounts import Account,SpecialAccount


# Now create some fictitious clients to test, we get 3 objects right here.
joao=Client("João da Silva","777-1234")
maria=Client("Maria Silva","555-4321")
jose=Client("José Vargas","433-4321")

# Put the objects creating accounts (can hava more than one people in a account)
names=[Account([[joao.name,maria.name],[joao.numb,joao.numb]],1,800),SpecialAccount([[jose.name],jose.numb],2,100,100)]

# Register the fictitious bank named "Tatú"
tatu=Bank("Tatú")

# now Tatú recives the clients account
for c in names:
    tatu.open_account(c)

# this is only to list the names and account number
def list():
    for counter in range(len(names)):
        print("{}-account number: {} - name:{}".format(counter, names[counter].contact[1], names[counter].contact[0]))

# Here is the core of operations, we choose what we want, following the options
while True:
    var=int(input("Main\n1-See the list accounts\n2-Deposit\n3-Withdraw\n4-Extract\n5-Abstract\n\n  Choose a option:"))
    if var==1:
        tatu.list_accounts()

    elif var==2:
        list()
        account_client=int(input("Choose account:"))
        names[account_client].deposit(float(input("Value:")))

    elif var==3:
        list()
        account_client = int(input("Choose account:"))
        names[account_client].withdraw(float(input("Value:")))


    elif var==4:
        account_client = int(input())
        names[account_client].extract()

    elif var==5:
        account_client = int(input())
        names[account_client].abstract()


    print("\n")


#
# acJM.withdraw(500)
# acJ.deposit(300)
# acJ.deposit(1500)
# acJM.deposit(100)
# acJ.withdraw(2000)
# acJ.withdraw(10)
# acJM.extract()
# acJ.extract()
# acJM.abstract()
# acJ.abstract()

