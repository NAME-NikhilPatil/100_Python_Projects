# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
import random

names_string = "Nikhil, Bob, Carol, David"
names = names_string.split(", ")
total_length = len(names)
choice = random.randint(0, total_length - 1)
print(f"{names[choice]} is going to buy the meal today!")

# Remember to remove the print statement above when you submit.
