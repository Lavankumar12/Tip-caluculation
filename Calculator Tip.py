#
# Tip Calculator
print("Welcome to the tip calculator")
total_bill_amount = int(input("What is the total bill amount?"))
tip = int(input("How much tip would you like to give? 5,10,15"))
people = int(input("How many persons would split the bill?"))
total_tip_amount = total_bill_amount * tip_as_percent
total_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${total_amount}")