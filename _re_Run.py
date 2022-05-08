############################################################################################
## Import packages
############################################################################################

from iqoptionapi.stable_api import IQ_Option
import time
import numpy as np
import numba as nb

############################################################################################
## Import files
############################################################################################

import JSON._reJson_UID as J

###############################################################################################
## Global Variables
###############################################################################################

App_still_running = True
Auto_trade_is_running = False
win_lose_count = 0

email = J.get_email()
password = J.get_password()

bot = IQ_Option(email,password)

###############################################################################################
## Function
###############################################################################################

def refresh_login():
    global bot
    email = J.get_email()
    password = J.get_password()
    bot = IQ_Option(email,password)
    bot.connect()

def run():
    global App_still_running
    while App_still_running:
        begin = time.time()
        bot.get_technical_indicators('EURUSD')
        print('latency = ',round(1000*(time.time()-begin)))
        begin = time.time()
        np.array([bot.get_technical_indicators('EURUSD')])
        print('\t\t\tnp latency = ',round(1000*(time.time()-begin)))

def buying():
    global bot
    global App_still_running

def stop_auto_trade():
    global Auto_trade_is_running
    global win_lose_count
    while True:
        if win_lose_count >= 0:
            Auto_trade_is_running = False
            print('Auto trade stopped')
            break
        time.sleep(5)
def martingale():
    global win_lose_count