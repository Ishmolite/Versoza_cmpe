'''
12/13/2025
WEEK 13 LESSON
NOTE***
All codes below are to be operated in mainProgram.py root file.
'''

#PART 1 =============================================================

import os
import time

print(os.getcwd())
print(os.listdir(os.getcwd()))

#os.dir simply lists down

'''Creating folders'''
print(os.makedirs(os.getcwd() + "/" + "New Folder 1"))
print(os.makedirs(os.path.join(os.getcwd(), "New Folder 2")))

'''Folder in a folder'''
os.makedirs(os.path.join(os.path.join(os.path.join(os.getcwd(), "New Folder 2")), "Folder in a Folder"))

'''Tells the current file you're running the command.'''
print(os.path.abspath(__file__))

'''Tells the directory of the file you're working in.'''
print(os.path.dirname(os.path.abspath(__file__)))

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

#PART 2 ----------------------------------------------

import os
import time
import csv

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #mainProgram as root
print(BASE_PATH)
BASE_PATH2 = os.path.dirname(BASE_PATH) #mainProgram in sub folder

RESOURCE_PATH = os.path.join(BASE_PATH, "RESOURCES")
CSV_PATH = os.path.join(RESOURCE_PATH, "MYFIRSTCSV.csv")

csv_list_data = []

with open(CSV_PATH, mode = "r", newline ='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_list_data.append(row)

print(csv_list_data)
print(csv_list_data[1])
print(csv_list_data[1][2])



'''Creating a new CSV file'''
name_and_address = []

for row in csv_list_data:
    name_and_address.append([row[1], row[4]])

CSV_PATH = os.path.join(RESOURCE_PATH, "NEWCSV.csv")

with open(CSV_PATH, mode = "w", newline ='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(name_and_address)


#PART 3-------------------------------------------------------

import os
import time
import gspread
from googleapiclient.errors import HttpError #google-api-python-client
from gspread.utils import ValueInputOption
from oauth2client.service_account import ServiceAccountCredentials

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #mainProgram as root
RESOURCE_PATH = os.path.join(BASE_PATH, "RESOURCES")
SERVICE_KEY_PATH = os.path.join(RESOURCE_PATH, "kinetic-catfish-481109-j1-5bca67d6561e.json")

sheet_url = "https://docs.google.com/spreadsheets/d/1oCSTHqfSayi6OmpiH7Q_FfpAfklDn71SiV_zzcTvtJE/edit?usp=sharing"

#Giving access and authorization to JSON Service Key credentials.
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY_PATH,
                scopes=['https://www.googleapis.com/auth/spreadsheets',  'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)


#Obtaining the data from the google sheet into console.
gs_instance = client.open_by_url(sheet_url)
sheet_instance = gs_instance.get_worksheet(0)
googlesheet_data = sheet_instance.get_all_records()
print(googlesheet_data)

#Inserting data from Pycharm to Google Sheet.
row_data = ["8", "Dorothy", "BSECE", "2-3", "Eden"]
sheet_instance.append_row(row_data)

