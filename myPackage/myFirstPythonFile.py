a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

try:
    mySum = int(a) + int(b) + int(c)
    print(mySum)
except ValueError:
    print("Wrong input.")

'''
This, right here, is a multi-line comment
I can go all day long!
Yeah, you heard me, all day long!!
'''

print("Hello World!")

doroInput = input("Do you love the dororong?")
input("Doro doro doro, doro " + doroInput + "?")
print(input("Dorodorodorodoro! "))
