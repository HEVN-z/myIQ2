from iqoptionapi.stable_api import IQ_Option
import time
import json
J = json.load(open("_reJSON_UID.json"))

email = J['username']
password = J['password']

bot = IQ_Option(email,password)

def run():
    for i in range(1):
        print("Running...")
        time.sleep(1)