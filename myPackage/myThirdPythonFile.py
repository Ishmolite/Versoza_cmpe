'''
10/25/2025
WEEK 7 LESSON
'''

#PART 1 --------------------------------------------------------------------------

#LIST
#CRUD CREATE READ UPDATE DELETE

fruitsA = [ "apple", "apple", "orange", "banana", "grapes" ]
print(fruitsA)

fruitsA.append("rambutan")
print(fruitsA)

fruitsA.insert(2,"lychee")
print(fruitsA)

print(fruitsA.index("banana"))
fruitsA[4] = "pineapple" #Indicates it is 4.
print(fruitsA)
print(len(fruitsA)) #Prints a 7, due to list length.
print(fruitsA.count("apple"))

fruitsA.remove("apple")
print(fruitsA)

print(fruitsA[4])

fruitsA.clear()
print(fruitsA)

#PART 2 -------------------------------------------------------------

#LIST
#CRUD - CREATE(append,insert) READ(view) UPDATE(assign value by index) DELETE (pop, remove, clear)

fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
fruitsB = ["banana", "mango", "lychee", "orange", "mango"]
fruitsC = ["mango", "grapes", "apple", "mango", "lychee"]

fruitBasket = [fruitsA, fruitsB, fruitsC] #list of lists
print(fruitBasket)
print(fruitBasket[2][3])

fruitBasketAdd = fruitsA + fruitsB + fruitsC #single list
print(fruitBasketAdd)

fruitsA.extend(fruitsB)
fruitsA.extend(fruitsC)
print(fruitsA) #single list

#LIST of a different data types and list
myInfoList = ["Versoza", 18, True, ["Doro", "Ishmael", "Silly"]]
print(myInfoList[0]) #prints Versoza (string)
print(myInfoList[1]) #prints 18 (integer)
print(myInfoList[2]) #prints True (boolean)
print(myInfoList[3]) #prints ['Doro', 'Ishmael', 'Silly'] (list)
print(myInfoList[3][1]) #prints Ishmael (string)

#PART 3 -------------------------------------------

#LIST
#CRUD - CREATE(append,insert) READ(view) UPDATE(assign value by index) DELETE (pop, remove, clear)

fruitsA = ("apple", "apple", "orange", "banana", "grapes")
print(fruitsA[3]) #prints banana
'''
NOT SUPPORT (item assignment), such as:
fruitsA[3] = "pineapple"
print(fruitsA[3])
'''
print(fruitsA.count("apple")) #prints 2
fruitsB = ("banana", "mango", "lychee", "orange", "mango")
fruitsC = ("mango", "grapes", "apple", "mango", "lychee")

fruitBasket = (fruitsA, fruitsB, fruitsC)
print(fruitBasket[2][4]) #prints lychee

#PART 4 ------------------------------------------------

#SETS { } CURLY BRACE

fruitsA = {"apple", "orange", "banana", "grapes"}
fruitsB = {"grapes", "apple", "mango","lychee"}
fruitsC = {"orange", "apple"}
fruitsD = {"cherry", "banana"}
#print(fruitsA)

fruitsUnion = fruitsA.union(fruitsB) #Unites all values into one.
print(fruitsUnion)
fruitsUnionB = fruitsA | fruitsB #Unites all values into one.
print(fruitsUnionB)

fruitsIntersection = fruitsA.intersection(fruitsB) #Takes the similarity.
print(fruitsIntersection)
fruitsIntersectionB = fruitsA & fruitsB #Takes the similarity.
print(fruitsIntersectionB)


fruitsDifference = fruitsA.difference(fruitsB) #Takes the difference.
print(fruitsDifference)
fruitsDifferenceB = fruitsA - fruitsB #Takes the difference.
print(fruitsDifferenceB)

#SUBSETS

fruitsA = {"apple", "orange", "banana", "grapes"}
fruitsB = {"grapes", "apple", "mango","lychee"}
fruitsC = {"orange", "apple"}
fruitsD = {"cherry", "banana"}

print(fruitsC.issubset(fruitsA)) #is fruitsC a subset of fruitsA (TRUE)
print(fruitsB.issubset(fruitsD)) #is fruitsB a subset of fruitsD (FALSE)

#PART 5 ---------------------------------------

# DICTIONARY - dict - CURLY BRACE, KEY-VALUE PAIR

myInfo = {
    'Name':'John Ishmol',
    'Age':18,
    'Gender':'Male'}

print(myInfo)

print(myInfo['Name'])
print(myInfo.get('Name'))
print(myInfo['Age'])
print(myInfo.get('Age'))
print(myInfo['Gender'])
print(myInfo.get('Gender'))

myInfo.update({"Age": 26}) #Update using update
print(myInfo)

myInfo["Age"] = 55 #Update using assign value
print(myInfo)

print(myInfo.values()) #Shows the values only
print(myInfo.keys()) #Shows the keys only

for i in myInfo.keys():
    print(myInfo[i])

#PART 6 -------------------------------------------

#myInfo = myInfo = {'Name':'John Ishmol', 'Age':18, 'Gender':'Male'}

myInfo = {
    "Name": {
        "First Name": "John",
        "Last Name": "Doe",
    },
    "Age": 23,
    "Citizenship": "American",
    "Hobbies": [
        "Being Silly", "Watching Documentaries", "Illustration"
    ]
}

print(myInfo)
print(myInfo["Name"]["First Name"])
print(myInfo["Name"]["Last Name"])
print(myInfo["Name"]["First Name"] + " " + myInfo["Name"]["Last Name"])
print(myInfo["Age"])
print(myInfo["Hobbies"][1])

myInfo["Name"]["First Name"] = "Doro"
print(myInfo["Name"]["First Name"])
print(myInfo["Name"]["First Name"] + " " + myInfo["Name"]["Last Name"])

#PART 7 -----------------------------------------------

myListofDictionary = [
    {"fruit" : "apple"},
    {"fruit" : "banana"},
    {"fruit" : "orange"}
]

print(myListofDictionary[2])
print(myListofDictionary[1]["fruit"])