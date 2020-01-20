import concurrent.futures as cf
import os
import time

def func(x, y):
    # time.sleep(3)
    print('Process ID:', os.getpid())
    time.sleep(3)
    return x*y

def processfunc():
    sum = 0
    for i in range(20):
        time.sleep(0.05)
        print(i)
        sum += i
    return sum

if __name__ == '__main__':

    executor = cf.ThreadPoolExecutor()
    future = executor.submit(func, 4, 5)

    print('Hello World!')

    # for i in range(5):
    #     print(i)

    res = future.result()
    print('func(x,y) Result:', res)


    # def processfunc():
    #     for i in range(20):
    #         time.sleep(0.1)
    #         print(i)

    e = cf.ProcessPoolExecutor()
    f = e.submit(processfunc)

    for i in range(10):
        time.sleep(0.1)
        print('Main:', i)
    print(f.result())
