#Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))
per_tip = int(input("What percentage tip would you like to give? 10, 12 or 15 ? "))

pay = ( (per_tip * total_bill / 100 ) + total_bill ) / num_people

print("Each person should pay: ", pay)