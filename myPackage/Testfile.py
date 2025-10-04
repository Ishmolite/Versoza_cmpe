from time import sleep

print("Accessing Data File Access...")
print('Request halted, Invalid Access. To proceed, fill in the necessary details.')

accessName = input("Requesting Access Name : ")

if accessName == "Ishmol":
    input("Are you sure you are " + accessName + "? ")
else:
    print("Access Denied.")



print("Initializing...")
print("Decrypting...")
sleep(2)
print("Providing access...")
sleep(0.5)
print("Access granted.")
print("Welcome, Ishmol")
