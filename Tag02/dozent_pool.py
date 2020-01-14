import os
from multiprocessing import Pool
import time

def quadfunc(n):
    time.sleep(0.2)
    return n*n

if __name__ == '__main__':
    print(os.cpu_count())

    t = time.time()
    p = Pool(processes = 5)
    result = p.map(quadfunc, [1, 2, 3, 4, 5])
    p.close()
    print('Pool time:', time.time()-t)

    t = time.time()

    result2 = list(map(quadfunc, [1, 2, 3, 4, 5]))
    print('Serial time:', time.time()-t)

    # print(result)
