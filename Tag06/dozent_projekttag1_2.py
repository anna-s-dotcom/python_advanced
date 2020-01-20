import multiprocessing as mp
import time

hole = mp.Value('f', 23.0)

def dig(amount, t, hole, lock):
    while True:

        lock.acquire()
        if hole.value >= 0:
            hole.value -= amount
            lock.release()
        else:
            lock.release()
            break
        time.sleep(t)

if __name__ == '__main__':
    lock = mp.Lock()
    t = time.time()
    a1 = mp.Process(target = dig, args = (1, 1, hole, lock))
    a2 = mp.Process(target = dig, args = (1.5, 1, hole, lock))
    a3 = mp.Process(target = dig, args = (1, 0.5, hole, lock))
    a4 = mp.Process(target = dig, args = (1.3, 0.7, hole, lock))
    a5 = mp.Process(target = dig, args = (0.8, 0.4, hole, lock))

    a1.start()
    a2.start()
    a3.start()
    a4.start()
    a5.start()

    a1.join()
    a2.join()
    a3.join()
    a4.join()
    a5.join()
    print('Benötigte Zeit:', time.time()-t)
