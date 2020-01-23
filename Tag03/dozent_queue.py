from multiprocessing import Process, Queue, current_process
from time import sleep

def putX(queue, x):
    for i in x:
        sleep(0.01)
        queue.put(i)

if __name__ == '__main__':
    q = Queue(maxsize = 5)

    p1 = Process(target = putX, args = (q, range(20)))
    p1.start()

    sleep(0.2)

    while not q.empty():
        sleep(0.02)
        print(q.get())
    p1.join()
    print('Ende')
