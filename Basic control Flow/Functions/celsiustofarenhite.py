def calculatefaranheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = calculatefaranheit(celsius)
print("Temperature in Fahrenheit:", fahrenheit)