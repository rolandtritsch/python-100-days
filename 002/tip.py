_amount = float(input("Enter the amount: "))
_tip = int(input("Enter the tip percentage: "))
_number_of_people = int(input("Enter the number of people: "))
_amount_per_person = _amount * (1 + _tip / 100) / _number_of_people
print(f"Each person should pay: {_amount_per_person:.2f}")
