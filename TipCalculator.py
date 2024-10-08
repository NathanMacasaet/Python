print("Welcome to tip Calculator")

#input
bill = float(input("What was the total bill?\n"))
people = int(input("How many people to split the bill?\n"))
tip = int(input("what percentage tip would you like to give?\n"))

#functions
TotalBill = tip / 100 * bill + bill
Tip_per_person = (float(TotalBill) / people) * tip
per_person = (float (TotalBill / people))
#output
print("Total : €" + "{:.2f}".format(TotalBill))
print("Each person should pay : €" + "{:.2f}".format(per_person))


