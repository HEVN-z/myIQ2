from json import load
from iqoptionapi.stable_api import IQ_Option
import logging
import time
import os
from dotenv import load_dotenv
load_dotenv()
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
bot=IQ_Option(os.getenv("email"),os.getenv("password"))
bot.connect()#connect to botoption

while_run_time=10

#For digital option

name="live-deal-digital-option" #"live-deal-binary-option-placed"/"live-deal-digital-option"
active="EURUSD"
_type="PT1M"#"PT1M"/"PT5M"/"PT15M"
buffersize=10#
print("_____________subscribe_live_deal_______________")
bot.subscribe_live_deal(name,active,_type,buffersize)


start_t=time.time()
while True:
    #data size is below buffersize
    #data[0] is the last data
    data=(bot.get_live_deal(name,active,_type))
    print("__For_digital_option__ data size:"+str(len(data)))
    print(data)
    print("\n\n")
    time.sleep(1)
    if time.time()-start_t>while_run_time:
        break
print("_____________unscribe_live_deal_______________")
bot.unscribe_live_deal(name,active,_type)


#For binary option

name="live-deal-binary-option-placed"
active="EURUSD"
_type="turbo"#"turbo"/"binary"
buffersize=10#
print("_____________subscribe_live_deal_______________")
bot.subscribe_live_deal(name,active,_type,buffersize)

start_t=time.time()
while True:
    #data size is below buffersize
    #data[0] is the last data
    data=(bot.get_live_deal(name,active,_type))
    print("__For_binary_option__ data size:"+str(len(data)))
    print(data)
    print("\n\n")
    time.sleep(1)
    if time.time()-start_t>while_run_time:
        break
print("_____________unscribe_live_deal_______________")
bot.unscribe_live_deal(name,active,_type)