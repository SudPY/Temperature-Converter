celsius = float(input("Enter temperature in Celsius : "))

fahrenheit = (celsius * 1.8) + 32

print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

temp = fahrenheit

if (temp >= 104):
    print("Temperature is hot!")
elif (temp < 50):
    print("Temperature is cold!")
else:
    print("Temperature is nice!")
