# simple function
def greet():
    print("Hello, I am Nikhil")


greet()


# fucntion which allows input
def greet_with_name(name):
    print(f"Hello, I am {name}")


greet_with_name("Nikhil")


# function with two parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Rohan", "Nallasopara")
greet_with(location="Dadar", name="Nikhil")
