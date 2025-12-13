'''
12/13/2025
WEEK 13 LESSON
'''

#PART 1 =============================================================
#File to be tested in root file "mainProgram.py"
import os
import time

print(os.getcwd())
print(os.listdir(os.getcwd()))

#os.dir simply lists down

'''Creating folders
print(os.makedirs(os.getcwd() + "/" + "New Folder 1"))
print(os.makedirs(os.path.join(os.getcwd(), "New Folder 2")))
'''
'''Folder in a folder
s.makedirs(os.path.join(os.path.join(os.path.join(os.getcwd(), "New Folder 2")), "Folder in a Folder"))
'''
'''Tells the current file you're running the command.
print(os.path.abspath(__file__))
'''
'''Tells the directory of the file you're working in.
print(os.path.dirname(os.path.abspath(__file__)))
'''
'''Checks a designated directory for a file.'''
BASE_PATH = (os.path.dirname(os.path.abspath(__file__)))

'''Creates a file in the specified directory'''
with open(os.path.join(BASE_PATH, "DORO.bat"), "w", encoding= "utf-8") as f:
    print("DORO has been created.")
    time.sleep(5)

#Checks every directory and file of the directory the program file is in
for root, dirs, files in os.walk(BASE_PATH):
    for filename in files:
        print(filename)
        if filename == "DORO.bat":
            print("==============================")
            print("DORO is present 😱😱😱😱")
            file_loc = os.path.join(root, filename)
            print(file_loc) #tells the directory of DORO.bat
            time.sleep(2)
            os.remove(file_loc) #deletes DORO.bat
            time.sleep(2)
            print("DORO is no more. 😔😔😔😔")
            print("==============================")



