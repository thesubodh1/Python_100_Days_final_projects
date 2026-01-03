print("Welcome to Tip Calculator")
total_bill = float(input("What is the total bill:- $"))
tip_percentage = int(input("How much tip would you like to give? 10,12 or 15 percentage:- "))
people = int(input("How many persons are going to share the bill:- "))


total_after_tip = total_bill + total_bill * (tip_percentage/100)
share_on_each = round(total_after_tip / people,2)
print(f"Each of you should pay ${share_on_each}")