from itertools import count
import time
from iqoptionapi.stable_api import IQ_Option
from dotenv import load_dotenv
import os
from os.path import join, dirname
#load_dotenv(join(dirname(__file__), '../.env'))
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
bot = IQ_Option(email,password)
bot.connect()#connect to iqoption
while True:
    if bot.connect():
        print("Connected")
        break
    else:
        print("Failed to connect")
        break
#print(bot.get_candles("EURUSD",60,1,time.time()))
'''ACTIVES="EURUSD"
duration=1
bot.subscribe_strike_list(ACTIVES,duration)
print(bot.get_all_profit()["EURUSD"]["turbo"])
print(bot.get_digital_current_profit(ACTIVES, duration))
bot.unsubscribe_strike_list(ACTIVES,duration)'''

'''bot.start_candles_stream("EURUSD",60,1,time.time())
while True:
    #print(bot.get_candles("EURUSD",60,1,time.time()))
    print(bot.get_realtime_candles("EURUSD",60))
    time.sleep(.2)'''

'''print(bot.get_balance(),bot.get_currency())
print(bot.get_balance_mode())
bot.change_balance("REAL")
print(bot.get_balance(),bot.get_currency())
print(bot.get_balance_mode())
bot.change_balance("PRACTICE")
print(bot.get_balance(),bot.get_currency())
print(bot.get_balance_mode())'''


country="TH"
from_position=1
to_position=10000
near_traders_count=0

print(bot.get_leader_board(country,from_position,to_position,near_traders_count))

