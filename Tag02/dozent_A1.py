# Erstelle eine Funktion die die Summe von a und b ausgibt und eine Sekunde dafür benötigt.
# Berechne die Summen  von (5,5), (10,5) und (10,10).
# Jede Funktion soll in einem eigenen Prozess parallel ausgeführt werden.

import multiprocessing as mp
import time

nums = [(5,5), (10,5), (10,10)]

def summe(a, b):
    time.sleep(0.1)
    print(a+b)

if __name__ == '__main__':
    # Class Process
    ps = []
    for num in nums:
        p = mp.Process(target = summe, args=num)
        ps.append(p)
        p.start()

    for p in ps:
        p.join()

    print('Process Ende')

    with mp.Pool(processes = 3) as p:
        p.starmap(summe, nums)

    print('Pool Ende')
