a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

try:
    mySum = int(a) + int(b) + int(c)
    print(mySum)
except ValueError:
    print("Wrong input.")