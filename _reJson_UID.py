import json
import time

json_file = json.load(open("_reJSON_UID.json"))


def get_email():
    json_file = json.load(open("_reJSON_UID.json"))
    return json_file["email"]

def get_password():
    json_file = json.load(open("_reJSON_UID.json"))
    return json_file["password"]

'''def set_amount(newamount):
    json_file["amount"] = newamount
    json.dump(json_file, open("_reJSON_UID.json", "w"))'''
