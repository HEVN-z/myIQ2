import time
from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
import os
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

bot = IQ_Option(email, password)
bot.connect()

while True:
    if bot.connect():
        print("Connected")
        break
    else:
        print("Failed to connect")

print("I am Online!")

def get_tech_ind_percentage(indicator, expire_time, type):
    items = [x for x in indicator if x["candle_size"] == expire_time and x["group"] == type]
    item_buy = sum(i["action"] == "buy" for i in items)
    item_hold = sum(i["action"] == "hold" for i in items)
    item_sell = sum(i["action"] == "sell" for i in items)
    total = item_buy + item_hold + item_sell
    return (item_buy - item_sell) / total * 100

def get_tech_i(active):
    indicator = bot.get_technical_indicators(active)
    osc1 = get_tech_ind_percentage(indicator, 60, "OSCILLATORS")
    osc5 = get_tech_ind_percentage(indicator, 300, "OSCILLATORS")
    osc15 = get_tech_ind_percentage(indicator, 900, "OSCILLATORS")
    osc60 = get_tech_ind_percentage(indicator, 3600, "OSCILLATORS")

    ma1 = get_tech_ind_percentage(indicator, 60, "MOVING AVERAGES")
    ma5 = get_tech_ind_percentage(indicator, 300, "MOVING AVERAGES")
    ma15 = get_tech_ind_percentage(indicator, 900, "MOVING AVERAGES")
    ma60 = get_tech_ind_percentage(indicator, 3600, "MOVING AVERAGES")

    av1 = (osc1 + ma1) / 2
    av5 = (osc5 + ma5) / 2
    av15 = (osc15 + ma15) / 2
    av60 = (osc60 + ma60) / 2
    return round(av1,2), round(av5,2), round(av15,2), round(av60,2)

while True:
    print(get_tech_i("EURUSD"))
    time.sleep(.2)

############################################################################################
## Import packages
############################################################################################

import json
import time


############################################################################################
## Load files
############################################################################################

json_file = json.load(open("_reJSON_UID.json"))

###############################################################################################
## Function
###############################################################################################

def get_email():
    json_file = json.load(open("_reJSON_UID.json"))
    return json_file["email"]

def get_password():
    json_file = json.load(open("_reJSON_UID.json"))
    return json_file["password"]


############################################################################################
## Write files
############################################################################################

def set_email(newemail):
    json_file["email"] = newemail
    json.dump(json_file, open("_reJSON_UID.json", "w"))

def set_password(newpass):
    json_file["password"] = newpass
    json.dump(json_file, open("_reJSON_UID.json", "w"))

