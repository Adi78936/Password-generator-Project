import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#password=""

#for i in range(0,nr_letters):
    #password+=random.choice(letters)

#for i in range(0,nr_symbols):
   # password+=random.choice(symbols)

#for i in range(0,nr_numbers):
   # password+=random.choice(numbers)

#random.shuffle(password)
#print(password)
#this wont give correct password as string doesn't shuffles like this in python.

passe = []
for i in range(0, nr_letters):
    passe.append(random.choice(letters))

for i in range(0, nr_symbols):
    passe.append(random.choice(symbols))

for i in range(0, nr_numbers):
    passe.append(random.choice(numbers))

print(passe)

random.shuffle(passe)

key = ""
for i in passe:
    key += i
print(key)

print("".join(passe))

print(f"Your final password is {key}")

# Password strength check
def check_strength(password):
    """Evaluates password strength"""
    length = len(password)
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_symbol = any(c in symbols for c in password)

    types_used = sum([has_letter, has_number, has_symbol])

    if length < 8 or types_used == 1:
        return "❌ Weak"
    elif length >= 12 and types_used == 3:
        return "✅ Strong"
    else:
        return "⚠️ Moderate"

# Call strength check on generated password
strength = check_strength(key)
print(f"📊 Password Strength: {strength}")
