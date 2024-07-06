print("Welcome to the Tip Calculator")
total = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give?10,12 or 15? "))
tip_value = total * (tip / 100)
total += tip_value
print(total)
split = int(input("How many people to spilt the bill? "))
each_will_pay = total / split
round(each_will_pay,2)
print(f"Each person should pay {each_will_pay}")
