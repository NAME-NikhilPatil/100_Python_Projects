################### Scope ####################

enemies = 1
player_health = 10
heroes = 1
# global constants
PI = 3.14


# use uppercase for globar variables so that it should not change-+


def increase_enemies():
    # global variable
    global heroes
    heroes += 1
    # local scope
    enemies = 2
    # global scope
    print(player_health)
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
