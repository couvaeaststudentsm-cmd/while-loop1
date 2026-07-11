import random

length = int(input("Enter password length: "))

lower = ""
upper = ""

for i in range(97, 123):   
    lower += chr(i)

for i in range(65, 91):    
    upper += chr(i)

digits = "0123456789"

all_characters = lower + upper + digits

password = [
    random.choice(lower),
    random.choice(upper),
    random.choice(digits)
]

for i in range(length - 3):
    password.append(random.choice(all_characters))

random.shuffle(password)

password = "".join(password)

print("Generated Password:", password)
