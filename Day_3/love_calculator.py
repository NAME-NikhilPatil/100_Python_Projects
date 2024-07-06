print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lowered_leters = combined_names.lower()
t = lowered_leters.count("t")
r = lowered_leters.count("r")
u = lowered_leters.count("u")
e = lowered_leters.count("e")
true_total = t + r + u + e
l = lowered_leters.count("l")
o = lowered_leters.count("o")
v = lowered_leters.count("v")
e = lowered_leters.count("e")
love_total = l + o + v + e

total_score = int(str(true_total) + str(love_total))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
