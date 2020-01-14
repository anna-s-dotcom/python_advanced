import os
import multiprocessing

def func(x):
    print(os.getpid())
    print(multiprocessing.current_process().pid)
    print()
    return __name__

# print(__name__)

def func2(a, b):
    return a*b

def hilf(x):
    return func2(x[0], x[1])

if __name__ == '__main__':
    func(0)
    with multiprocessing.Pool() as p:
        res = p.map(func, range(4))
    print(res)

    # funktioniert nicht mit lambda da er lambda in den child prozessen nicht kennt
    with multiprocessing.Pool() as p:
        # prod = p.map(hilf, [(1,2), (4,2), (3,6)])
        prod = p.starmap(func2, [(1,2), (4,2), (3,6)])
    print(prod)
