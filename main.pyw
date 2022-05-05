import time
from threading import Thread
from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
import server.server_gui as gui
print("Loading .env file...")
import os

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

Thread(target = gui.main_gui).start()

bot = IQ_Option(email, password)
bot.connect()

while True:
    if bot.connect():
        print("Connected")
        break
    else:
        print("Not connected")
        bot.connect()
    time.sleep(1)

print(bot.get_balance())
print(bot.get_balance_mode())
print(bot.get_balance_id())
