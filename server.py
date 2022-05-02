from functools import cache
import time
from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
import os
import json
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

bot = IQ_Option(email, password)
'''
bot.connect()

while True:
    if bot.connect():
        print("Connected")
        break
    else:
        print("Failed to connect")

print("I am Online!")
'''
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    }
}
dict1['emp3'] = {'name':"HEVNz"}
try:
    r = json.load(open("_json.json"))
except:
    pass
w = open("_json.json", "w")
json.dump(dict1, w, indent=4)



print(r['emp2'])
#while True:
