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

