import random
import string

print("----- Password Generator -----")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Characters to use in password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for i in range(length))

# Display password
print("\nGenerated Password:", password)
