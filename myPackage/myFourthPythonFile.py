'''
11/08/2025
WEEK 10 LESSON
'''

#PART 1 -------------------------------------------------------

myGrade = 92

if myGrade >= 97:
    print("Grade is: 1.0")

# elif myGrade >= 94 and myGrade <= 97: (REDUNDANT)
elif myGrade >= 94:
    print("Grade is: 1.25")
elif myGrade >= 91:
    print("Grade is: 1.50")
elif myGrade >= 88:
    print("Grade is: 1.75")
elif myGrade >= 85:
    print("Grade is: 2.00")
elif myGrade >= 82:
    print("Grade is: 2.25")
elif myGrade >= 79:
    print("Grade is: 2.50")
elif myGrade >= 76:
    print("Grade is: 2.75")
elif myGrade >= 75:
    print("Grade is: 3.00")
else:
    print("Grade is: 5.00")

print("After If Else Condition")

#PART 1.2 -------------------------

shapeofyou = "square"

if shapeofyou.lower() == "rectangle":
    print("Rectangle")
elif shapeofyou.lower() == "triangle":
    print("Triangle")
elif shapeofyou.lower() == "square":
    print("Square")
else:
    print("Unknown")

print("Waiter, waiter! Next question Please!!")

#PART 2 -------------------------------------------------------

#ELIGIBLE TO VOTE - CHECKER
age = input("Please enter your age: ")
citizenship = input("Please enter your citizenship: ")
residency = input("How long have you been in residence? ")
isregistered = input("Are you a registered voter? ")

#nested, if else within if, else, elif

if citizenship == "Filipino" and int(age) >= 18 and int(residency) >= 6:
    if isregistered == "yes" or "Yes":
        print("You can vote! Amazing!")
    else:
        print("You can't vote, but you can register today!")
elif citizenship == "Filipino" and int(age) < 18 and int(residency) >= 6:
    print("You're too young to vote!!")
elif citizenship == "Filipino" and int(age) >= 18 and int(residency) < 6:
    print("Your residence duration is not enough for you to vote!!")
else:
    print("You cannot vote or register, get out!!!")

#PART 3 -------------------------------------------------------

#for (int x =0; x < 10; x++) {

for x in range(0, 10, 1): #Initial (default 0), limit, interval (increment/decrement)
    print(x)
print("after loop1")
#----------------------------------------------
print("before loop2")
for x in range(10):
    print(x)
print("after loop2")
#----------------------------------------------
print("before loop3")
for x in range(0, 10):
    print(x)
print("after loop3")
#----------------------------------------------
print("before loop4")
for x in range(10, 1):
    print(x)
print("after loop4")
#----------------------------------------------

#PART 3.1 -------------------------

fruitsList = ["apple", "orange", "banana", "cherry"]

for eachFruit in fruitsList:
    print("Fruit List includes : " + eachFruit)

myWord = "Pneumonoultramicroscopicsilicovolcanoconiosis"

for char in myWord:
    print(char.upper())

#DICTIONARY
myInfo = {
    "Name" : "Versoza",
    "Age" : 18,
    "School" : "PUP"
}

for anyKey in myInfo:
    print(anyKey) #prints Name, Age, School

for anyValues in myInfo.values():
    print(anyValues) #prints Versoza, 18, PUP

for anyKey in myInfo:
    print(anyKey, myInfo[anyKey])

#TUPLE

myTuple = ("hello", "world", "universe", "rather")
for eachTuple in myTuple:
    print(eachTuple)

#SET

mySet = {"hello", "world", "universe", "rather"}
for eachTuple in mySet:
    print(eachTuple)

#PART 4  -------------------------------------------------------

import time

isConnected = "no"

for i in range(4):
    time.sleep(2)
    isConnected = input("Are you connected? (yes/no) ")
    if isConnected == "yes":
        print("Connection is successful")
        break #Ends the simulation.
    else:
        print("Request Timeout")

print("Processing...")

#PART 4.1------------------------

myList = ["Yes",  "no", "Yes", "Yes"]

for x in myList:
    if x == "no":
        continue
    print(x)
    print("pasok")
    print("klase")
    print("uwi")

#----

#nest of loop
for x in range(10): #outer loop
    print(str(x) + "====================")
    for y in range(10): #inner loop
        print (y)

#----
myString = "tattarrattat"
newValue = ""

for char in myString:
    newValue = char + newValue

print(newValue)

if myString.lower() == newValue.lower():
    print("PALINDROME")
else:
    print("NOT PALINDROME")

#PART 5  -------------------------------------------------------

charList = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9',  " ", "!", "@", "#", "$", "%", "^", "&", "*", "(",
")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'",
'"',",", "<", ".", ">", "/", "?", "\\", "|", "`", "~"]

key = 5
inputMessage = "My Pin Number is 12345"
outputMessage = "" #"RD%Uns%Szrgjw%nx%6789" if inputMessage = 5
indexCounter = 0

for letter in inputMessage:
    indexCounter = charList.index(letter)
    print(indexCounter)
    outputMessage = outputMessage + charList[indexCounter + key]


print(outputMessage) #------> network

'''
Resolve the possible index error
Suggested solution:
    Once the outputMessage value exceeds the list index value number,
    return to the beginning.
'''