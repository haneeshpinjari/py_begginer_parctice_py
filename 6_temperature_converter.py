def celsius_to_fahrenheit(celsius):
    return (celsius + 9 / 5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("convert to (C)elsius or (F)ahrenheit? : ").lower()
if choice == 'f':
    celsius = float(input("Enter temperature in celsius: "))
    print(f"{celsius} ℃ is {celsius_to_fahrenheit(celsius)} ℉ ")
elif choice == 'c':
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    print(f"{fahrenheit} ℃ is {fahrenheit_to_celsius(fahrenheit)}℉")
else:
    print("Invalid option")