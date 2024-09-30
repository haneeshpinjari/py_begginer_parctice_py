def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter the number: "))
if isprime(number):
    print(f"{number} is aprime number")
else:
    print(f"{number} is a not aprime number.")