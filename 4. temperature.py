def convert_cel_to_far(celsius):
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

degrees_fahrenheit = float(input("Enter a temperature in degrees F: "))
print(f"{degrees_fahrenheit} degrees F = {convert_far_to_cel(degrees_fahrenheit):.2f} degrees C")
degrees_celsius = float(input("Enter a temperature in degrees C: "))
print(f"{degrees_celsius} degrees C = {convert_cel_to_far(degrees_celsius):.2f} degrees F")
