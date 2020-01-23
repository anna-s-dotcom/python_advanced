# Erstelle zwei funktionen. Eine, die zu einer Zahl 2 hinzu addiert und eine, die von einer Zahl 2 abzieht.
#
# Erstelle einen shared Value Datentyp mit dem Wert 100.
#
# Erstelle für jede Funktion je 20 Prozesse, die diese Funktion aufrufen.
#
# Gib den Endwert der shared Value Variable aus.
#
# Bonus: Teste Zeit mit Lock und Zeit ohne Lock.
import multiprocessing as mp
import time

def plus2(x):
    x.value += 2

def minus2(x):
    x.value -= 2

def plus2lock(x, lock):
    lock.acquire()
    x.value += 2
    lock.release()

def minus2lock(x, lock):
    lock.acquire()
    x.value -= 2
    lock.release()

if __name__ == '__main__':
    shared_value = mp.Value('i', 100)

    processes = []
    t = time.time()
    for i in range(20):
        p1 = mp.Process(target = plus2, args=(shared_value, ))
        p2 = mp.Process(target = minus2, args=(shared_value, ))
        processes.append(p1)
        processes.append(p2)
        p1.start()
        p2.start()

    for p in processes:
        p.join()

    print('Without Lock:', time.time()-t)
    print(shared_value.value)
    print()

    shared_value = mp.Value('i', 100)
    processes = []

    t = time.time()
    lock = mp.Lock()
    for i in range(20):
        p1 = mp.Process(target = plus2lock, args=(shared_value, lock))
        p2 = mp.Process(target = minus2lock, args=(shared_value, lock))
        processes.append(p1)
        processes.append(p2)
        p1.start()
        p2.start()

    for p in processes:
        p.join()

    print('With Lock:', time.time()-t)
    print(shared_value.value)
    print()

    print(type(shared_value.value))
