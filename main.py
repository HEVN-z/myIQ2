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

while True:
    indi = bot.get_technical_indicators("EURUSD")
    print(indi)
    time.sleep(.2)