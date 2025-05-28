import random

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"
]

first_name = input("Enter your first name: ")
random_last_name = random.choice(last_names)

print(f"Your generated name is: {first_name} {random_last_name}")