import time
item = [5,4,3,2,1]
#while True:
tempitem = []
for x in item:
    #rint(item.index(x))
    newpos = item.index(x)-1
    if newpos<0:
        x = None
    tempitem.insert(newpos,x)
print(tempitem)