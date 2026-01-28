import random

def generate_password():
    return str(random.randint(100000,999999))
print(generate_password())