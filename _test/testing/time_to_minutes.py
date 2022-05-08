import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370)))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

print(time.strftime('%H:%M:%S', time.localtime(time.time())))