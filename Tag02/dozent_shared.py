import multiprocessing as mp

def shared_double(d, lock):
    lock.acquire()
    d.value *= 2
    lock.release()

def shared_tripple(t, lock):
    lock.acquire()
    t.value *= 3
    lock.release()





if __name__ == '__main__':
    v = mp.Value('f', 5.0)
    lock = mp.Lock()
    print(v)
    print(v.value)

    p1 = mp.Process(target = shared_double, args=(v, lock))
    p2 = mp.Process(target = shared_tripple, args=[v, lock])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(v)
    print(v.value)
