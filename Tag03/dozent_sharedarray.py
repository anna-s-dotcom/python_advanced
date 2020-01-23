from multiprocessing import Process, Array, Lock
import time

def plus2(x, i):
    x[i] += 2

def plus2arr(x, lock):
    t = time.time()
    for i in range(len(x)):
        lock.acquire()
        x[i] += 2
        lock.release()
    print('In For Loop', time.time()-t)


def plus2arr2(x, lock):
    t = time.time()
    lock.acquire()
    for i in range(len(x)):
        x[i] += 2
    lock.release()
    print('Out For Loop', time.time()-t)

if __name__ == '__main__':

    arr = Array('i', 40000)
    # print(arr[:])
    lock = Lock()

    # arr2 = Array('f', range(4))
    # print(arr2[:])

    # p1 = Process(target = plus2, args = (arr, 0))
    # p1.start()
    p2 = Process(target = plus2arr, args = (arr, lock))
    p2.start()
    p3 = Process(target = plus2arr2, args = (arr, lock))
    p3.start()

    # p1.join()
    p2.join()
    p3.join()

    # print(arr[:])
    # print(type(arr))
    # print(type(arr[0]))
