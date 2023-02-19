print("Welcome to the tip calculator.")

bill = int(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
people = int(input("How many people split the bill?\n"))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
people_bill = total_bill / people
final = "{:.2f}".format(people_bill)

print(f"Each person should pay: ${final}")
