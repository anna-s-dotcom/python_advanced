import concurrent.futures as cf
from multiprocessing import Pool
import os
import time


def func(x, y):
    # time.sleep(3)
    print('Hello from', os.getpid())
    return(x*y)

if __name__ == '__main__':
    args = range(5)

    e = cf.ProcessPoolExecutor(max_workers = 5)
    f = e.map(func, range(5), range(10, 15))
    for i in range(100):
        print(i)
    print(list(f))
    # from multiprocessing import Pool
    args = range(5)

    p = Pool(processes = 5)
    result = p.starmap(func, zip(range(5), range(10, 15)))
    for i in range(100):
        print(i)
    print(result)
    p.close()
