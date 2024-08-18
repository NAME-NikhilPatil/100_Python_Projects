numbers = [20, 10, 20, 30, 50]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
#
# print(new_list)

# using list comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Nikhil"
new_list = [letter for letter in name]
print(new_list)

new_range = [i + 2 for i in range(1, 5)]
print(new_range)

# Conditional list comprehension
names = ["Nikhil", "Talha", "Mayur", "Niku", "Niki"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
capital_names = [name.upper() for name in names if len(name) > 4]
print(capital_names)
