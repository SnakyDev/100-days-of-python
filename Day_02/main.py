print("SnakyDev - Tip calculator \n")

total_bill = float(input("What is the total bill? R"))
tip_percentage = float(input(
    "\nWhat percetange would you like to give your waiter? 10%, 15% or 20% "))
number_of_people = float(input("\nHow many people to split the bill? "))

tip_amount = (tip_percentage/100) * total_bill
bill_per_person = (tip_amount + total_bill)/number_of_people

print(f"\nEach person should pay R{round(bill_per_person, 2)}")
print("\nThank you for using SnakyDev-Tip calculator!\n")
