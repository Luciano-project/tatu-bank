class Bank:
    def __init__(self, name):
        self.name=name
        self.clients=[]
        self.accounts=[]

    def open_account(self,account):
        self.accounts.append(account)

    def list_accounts(self):
        for c in self.accounts:
            c.abstract()