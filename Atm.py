class atm :
    def __init__(self,Firstname,Lastname,balance,withdrawl) :
        self.Firstname=Firstname
        self.Lastname=Lastname
        self.balance=balance
        self.withdrawl=withdrawl
    def calculate(self) :
        self.balance=self.balance-self.withdrawl
    def show(self):
        print("Hi %s" % self.Firstname+''+self.Lastname)
        print("Now your balance is %d" % self.balance)
ATM=atm(input("Your First Name : "),input("Your Last Name : "),200000,int(input("How much money you want to withdraw : ")))
ATM.calculate()
ATM.show()

        
    
