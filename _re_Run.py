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

import _reJson_UID as J

###############################################################################################
## Global Variables
###############################################################################################

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
    while True:
        begin = time.time()
        bot.get_technical_indicators('EURUSD')
        print('latency = ',round(1000*(time.time()-begin)))
        begin = time.time()
        np.array([bot.get_technical_indicators('EURUSD')])
        print('\t\t\tnp latency = ',round(1000*(time.time()-begin)))
