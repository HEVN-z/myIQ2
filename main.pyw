import time
from threading import Thread
from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
from pip import main
import server.server_gui as g
print("Loading .env file...")
import os

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

Thread(target = g.mGUI).start()

bot = IQ_Option(email, password)
start_time = time.time()
bot.connect()
print("Connect time: ", round(time.time() - start_time,4) ,'second')
try:
    g.mGUI.lb.configure(text = "Connect time: " + str(round(time.time() - start_time,4)) + " second")
except Exception as e:
    print (e)

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
