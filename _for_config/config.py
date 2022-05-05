import json

load = json.load(open("config.json"))
candles = json.load(open("candles.json"))

set_a = load[0]['set_a']
set_b = load[0]['set_b']

check = []

a = candles[set_a]
b = candles[set_b]

condition = []

def condition(con):
    for c in con:
        if check[0]['enable'] == True:
            if check[0]['symbol'] == '<':
                return a < b
            elif check[0]['symbol'] == '>':
                return a > b

