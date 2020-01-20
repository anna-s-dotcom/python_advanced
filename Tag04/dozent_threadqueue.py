import threading as td
from queue import LifoQueue, Queue
import itertools as it
from time import sleep

def putStuff(q):
    counter = it.count()
    for i in counter:
        q.put(i)
        sleep(0.01)

lifoq = LifoQueue(maxsize = 0)
fifoq = Queue()

t = td.Thread(target = putStuff, args = (lifoq, ), daemon = True)
t.start()

t2 = td.Thread(target = putStuff, args = (fifoq, ), daemon = True)
t2.start()

print()
print('Lifo:')
for i in range(10):
    sleep(0.16)
    print('size', lifoq.qsize())
    print('last element in q:', lifoq.get())

print()
print('Fifo:')
for i in range(10):
    sleep(0.16)
    print('size', fifoq.qsize())
    print('last element in q:', fifoq.get())
