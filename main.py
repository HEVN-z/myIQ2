import time
from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
import os
import json
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

bot = IQ_Option(email, password)
bot.connect()

while True:
    print(bot.get_balance())
    print(bot.get_balance_mode())
    print(bot.get_balance_id())
    time.sleep(1)
