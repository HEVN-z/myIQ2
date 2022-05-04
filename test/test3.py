import numpy as np
dict = {}
dict['Capital']={"London":[1,2,3,4,5,6]}
dict['Food']="Fish&Chips"
dict['2012']="Olympics"

#lists
temp = []
dictList = []

#My attempt:
'''for key, value in dict.items():
    aKey = key
    aValue = value
    temp.append(aKey)
    #temp.append(aValue)
    dictList.append(temp) 
dictList = dictList[0]
print(dictList)'''

for key in dict.keys():
    dictList.append(key)

print(dictList)
