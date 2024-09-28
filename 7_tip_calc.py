bill = float(input("enter the bill amount: "))
tip_percent = float(input("enter the tip %: "))

tip_amount  = bill * (tip_percent / 100)
total_amount = bill + tip_amount

print(f" Tip amount : ₹{ tip_amount: .2f}")
print(f" Total amount :₹{ total_amount: .2f}")