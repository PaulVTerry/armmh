#a/r money market hedge

AR = 400000.0
ForeignBorrowRate = .09
SpotRate = 1.48
DomesticInvestmentRate = .08

MMHtest = (AR/ (1 + ForeignBorrowRate) * SpotRate) * (1 + DomesticInvestmentRate)

print "test", MMHtest


#use code above to check accuracy of code below
#-------------------------------------------------------------------------------
#use code below in CLI

AR = float(input("Amount of Accounts Receivable?"))
ForeignBorrowRate = float(input("What is the Foreign Interest (borrowing) Rate?"))
SpotRate = input("what is the spot rate?")
DomesticInvestmentRate = input("What is the Domestic Investment Rate?")

MMH = (AR/ (1 + ForeignBorrowRate) * SpotRate) * (1 + DomesticInvestmentRate)
print "Your Money Market Hedge is", MMH
