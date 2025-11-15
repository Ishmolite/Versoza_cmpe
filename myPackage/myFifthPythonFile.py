'''
11/15/2025
WEEK 11 LESSON
'''


#PART 1 -------------------------------------------------------
#function is a reusable block of code
#built in functions
#user defined functions


#function without parameter, and without return

import time
def welcome_messages():
    for i in range(10, 0 ,-1):
        print("Counter:" + str(i))
        time.sleep(0.2)

welcome_messages()

#function with parameter, but without return

def welcome_messages_with_input(message):
    for i in range(10, 0 ,-1):
        print("Counter:" + str(i))
        time.sleep(0.2)
    print(message)

welcome_messages_with_input("Happy New Year!!!")

#function without parameter, but with return

def welcome_messages():
    message = ""
    for i in range(10, 0 ,-1):
        message = message + " " + str(i)
        time.sleep(0.2)
    return message

print(welcome_messages())

#function with parameter and return

def welcome_messages(message):
    for i in range(10, 0 ,-1):
        message = message + " " + str(i)
        time.sleep(0.2)
    return message

print(welcome_messages("This is my input"))

#SAMPLE RETURN
a = 5
b = 25
c = 15
d = 45

def get_the_sum(inputA, inputB):
    sum = inputA + inputB
    return sum

finalSum = get_the_sum(a, b) + get_the_sum(c, d)
print(finalSum)

print(get_the_sum(get_the_sum(a, b), get_the_sum(c, d)))

#PART 2 -------------------------------------------------------

import time

def dororongs():
    """This function is a sample code for Continue and Return."""
    for i in range(0, 100, 1):
        message = "Finished!!!!!!"
        time.sleep(0.1)
        if i == 25:
            continue
        elif i == 75:
            return message
        print("Value of i is: " + str(i))
    return None

print(dororongs())

#PART 3 -------------------------------------------------------

listofnumbers = [25, 33, 45, 67, 90]

def add_function(a, b):
    """This function is used to add two numbers and return sum"""
    return a + b

def average_functions(inputList):
    """This function is used to get and return average"""
    totalsum = 0
    for i in inputList:
        totalsum = add_function(totalsum, i)
    average = totalsum / len(inputList)
    return average

print(average_functions(listofnumbers))