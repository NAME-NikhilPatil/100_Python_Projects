name_dictionary = {"nikhil": "Funny", "talha": "serious"}

# Retrieving items from dictinary
print(name_dictionary["nikhil"])

# Adding new items in dictinary
name_dictionary["Mayur"] = "Awesome"
print(name_dictionary)

# create an empty dictionary
empty_dictionary = {}

# wipe an exsisting dictionary
# name_dictionary = {}
# print(name_dictionary)

# Edit an existing dictionary
name_dictionary["nikhil"] = "Curious"
print(name_dictionary)

for key in name_dictionary:
    print(key)
    print(name_dictionary[key])
