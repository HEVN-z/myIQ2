import json

json_file = json.load(open("_automartingale.json"))
json_amount = json_file["amount"]


def get_amount():
    return float(json_file["amount"])


def set_amount(newamount):
    json_file["amount"] = newamount
    json.dump(json_file, open("_automartingale.json", "w"))
