import threading as td


def plus2(l):
    global total

    l.acquire()
    total += 2
    l.release()

total = 0
print(total)

lock = td.Lock()
t = td.Thread(target = plus2, args= (lock, ))
t.start()
t.join()

print(total)

from multiprocessing.pool import ThreadPool
import os

def poolfunc(x):
    print(td.current_thread().name)
    print('Prozess ID in Thread', os.getpid())
    return x+5

print('Prozess ID in Main', os.getpid())

t = ThreadPool(processes = 2)
result = t.map(poolfunc, [1, 2, 3])

print(result)
