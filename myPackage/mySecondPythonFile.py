'''
10/11/2025
WEEK 5 LESSON
'''

# PART 1 ------------------------------

strFullName = "Versoza Edison"
intLength = len(strFullName) #len for length

print(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[6])
print(strFullName[7])
print(strFullName[8])
print(strFullName[13])
print(strFullName[intLength-1])

mySubString = strFullName[2:5:2] #[start included, end excluded, step]
print(mySubString)

# PART 2 ---------------------------------------

strFullName = "Versoza Edison"

#String Method

newValue = strFullName.upper()
print(newValue)

newValue = strFullName.lower()
print(newValue)

newValue = strFullName.title()
print(newValue)

newValue = strFullName.capitalize()
print(newValue)

newValue = strFullName.split(" ")
print(newValue)

newValue = strFullName.split("er")
print(newValue)

newValue = strFullName.replace("Versoza","Dororong")
print(newValue)

newValue = strFullName.replace("Versoza"," ")
print(newValue)

myLastName = "Versoza"
myFirstName = "Edison"
myMiddleName = "Bautista"

myFullNameList = [myLastName, myFirstName, myMiddleName]
print("Doro Lover".join([myLastName, myFirstName, myMiddleName]))
print("Ishmolite".join(myFullNameList))

newValue =strFullName.count("Versoza")
print(newValue)

newValue = strFullName.index("o")
print(newValue)

#PART 3 --------------------------------------------------------

#STRING

'''
Numeric types:
Integer -10, 0, 2324
Float 25.2323
Complex 25+47j (i ampere, j impendance -> resistance + reactance)
'''
import math

intA = 25
intB = 15
intC = 5
intD = 2
intE = 2
myComA = 25+5j
myComB = 10-10j
comProd = myComA * myComB
print(comProd)
#arithmetic operations
intSum = intA + intB + intC
print(intSum)
intDiff = intA - intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQu = intA / intB
print(intQu)
intResult = intD ** intE
print(intResult)
#PMDAS

#cosine, sine, tangent
intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5
factResult = math.factorial(intX)
print(factResult)

'''
Comparison Operator
==, >, <, >=, <=, !=
Boolean data types are 'True or False'
  >> 'True' or 'False' = String
  >>'1' or '2' = Integer
'''

intA = 5
intB = 6

isResult = intA == intB
print(isResult)

isResult = intA <= intB
print(isResult)

isResult = intA >= intB
print(isResult)

isResult = intA > intB
print(isResult)

isResult = intA < intB
print(isResult)

isResult = intA != intB
print(isResult)

#PART 4 -------------------------------------------

#membership operator in, not in (CONTAINS)
isResult = "e" in "Madagascar"
print(isResult) #false
isResult = "e" not in "Madagascar"
print(isResult) #true
myList = ["Dorothy", "Lappland", "A2", "Amiya", "Hong Lu"]
isResult = "Ishmael" in myList
print(isResult) #false
myList = ["Dorothy", "Lappland", "A2", "Amiya", "Hong Lu"]
isResult = "Lappland" in myList
print(isResult) #true

#identity operator is, is not (EXACT)
isResult = "doro" is "dorothy"
print(isResult) #false
isResult = "doro" is not "dorothy"
print(isResult) #true

isMyResult = isResult is True
print(isMyResult)

#PART 5 ----------------------------------------------------

from traceback import print_tb

myInput = "1231231hello213123 2541wo2312rl2131d"

myOutput = ""

for char in myInput:
    if not char.isnumeric():
        myOutput = myOutput + char

print(myOutput)

#PART 6 ----------------------------------------------------

'''
LOGICAL OPERATORS
Not, and, or -------- nand, nor, exor, exnor
Logic circuits and switching theory
'''

isGroupPassed = False

passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86

isMarkPassed = markGrade >= passingGrade
isJennyPassed = jennyGrade >= passingGrade
isArthurPassed = arthurGrade >= passingGrade

isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed) #False, because one of them failed.

isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed) #True, because at least one of them passed.

# PART 7 ------------------------------------------------------

intA = 555
intB = 4
intC = 5

isDivisible = False #Initial Value
remainder = intA % intB #modulus or % returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True
    print(isDivisible) #False, remainder 3

isDivisible = False #Initial Value
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
    print(isDivisible) #True, remainder 0

