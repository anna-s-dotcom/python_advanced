import threading as td
import itertools as it
import time

def func():
    global counter
    counter = it.count()

    for i in counter:
        print('counter squared:', i*i)
        time.sleep(0.3)
        if i > 14:
            break
    counter = 'hey'


t = td.Thread(target = func)
t.daemon = True
t.start()


for i in counter:

    time.sleep(0.4)
    print('counter not squared', i)
    if i > 10:
        break

t.join()
print(counter)
print('End of Main')
