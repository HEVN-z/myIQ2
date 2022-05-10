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

def update_paired(pair,mode):
    global bot

def thread_if_remaining():
    global App_still_running
    global Auto_trade_is_running
    bot.start_candles_stream("EURUSD", 60, 1)
    before_to = 0
    # while App_still_running:
    #     c = bot.get_realtime_candles("EURUSD", 60)
    #     new_to = c[list(c.keys())[-1]]['to']
    #     if new_to != before_to:
    #         before_to = new_to
    #         J.set_remain_offset(bot.get_remaning(1)-30)
    #     # if bot.get_remaning(1) == 80:
    All = bot.get_all_open_time()
    # All_turbo = [i for i in All['turbo'] 
    #             if i['open'] == True]
    # for x in All['binary']:
    #     print(x + ' is ' +x['open'])
    # for i in All['binary']:
    #     pass
                #print(i)
    # print(All["turbo"])
        # time.sleep(.2)