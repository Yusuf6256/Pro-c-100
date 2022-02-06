class Atm(object):
    def __init__(self,atmcardnumber,pinnumber,balance):
        self.atmcardnumber = atmcardnumber
        self.pinnumber = pinnumber
        self.balance = balance


    def cashwithrawl(self):
        input("card Number: ")


    def balanceenquiry(self):
        print("Balance is: ",balance - cashwithdrawl)

balance = 50000
cashwithdrawl = int(input("amount of money: "))
axisbank = Atm("atmcardnumber","pinnumber","balance")
axisbank.cashwithrawl()
axisbank.balanceenquiry()