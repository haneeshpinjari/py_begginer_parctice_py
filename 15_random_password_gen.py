import random
import string

length = int(input("Enter the password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print(f"Generated password: {password}")
