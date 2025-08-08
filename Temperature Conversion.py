temp = float(input("Enter temperature: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit):").upper()

if unit == "C":
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result:.1f}°F")
elif unit == "F":
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result:.1f}°C")
else:
    print("Not a Valid Unit.")