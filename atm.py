class Atm(object):
    def __init__(self, company, location):
        self.company = company
        self.location = location
        self.userCardNum = 0
        self.userPinNum = 0
        self.userBal = 0
    
    def readCard(self, cardNum, pinNum, bal):
        self.userCardNum = cardNum
        self.userPinNum = pinNum
        self.userBal = bal
    
    def cashDeposit(self, d):
        self.userBal += d
        print("youve deposited $" + str(d) + " to your account")
    
    def cashWithdrawl(self, w):
        self.userBal -= w
        print("youve withdrawn $" + str(w) + " from your account")

    def balanceEnquiry(self):
        print("your balance is $" + str(self.userBal))

atm = Atm("Chase Bank", "Houston, Texas")
print(atm.company)
print(atm.location)
atm.readCard(1234, 5678, 350)
print(atm.userCardNum)
print(atm.userPinNum)
print(atm.userBal)

atm.cashDeposit(100)
print(atm.userBal)
atm.cashWithdrawl(50)
print(atm.userBal)

atm.balanceEnquiry()