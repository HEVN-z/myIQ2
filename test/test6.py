from iqoptionapi.stable_api import IQ_Option
import numpy as np
import time
import os
from dotenv import load_dotenv
load_dotenv()
np.set_printoptions(suppress=True)
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

bot = IQ_Option(email, password)
bot.connect()

print(bot.get_balance())

bot.start_candles_stream("AUDJPY",60,5)
isBuy = False
while True:
    #print(bot.get_candles("EURUSD",60,1,time.time()))
    candles = bot.get_realtime_candles("AUDJPY",60)
    ls = np.array([])
    close = np.array([])
    open = np.array([])
    for timestamp in candles:
        open = np.append(open, candles[timestamp]['open'])
        close = np.append(close, candles[timestamp]['close'])
        ls = close - open
        #invert = np.where(ls > 0, 1, 0)
        ls = ls * 10000
        rb = np.where(ls > 0, 'G','R')
        #inv = ls * -1
    if bot.get_remaning(1) == 61 and isBuy == False:
        print(rb[-3])
        print(rb[-2])
        print(rb[-1])
        isBuy = True
    #print(inv)
    if bot.get_remaning(1) == 35:
        isBuy = False
    #print(bot.get_remaning(1))
    time.sleep(.1)