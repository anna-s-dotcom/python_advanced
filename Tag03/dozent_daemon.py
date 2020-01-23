from time import sleep
import threading as td

def stack(time, amount, laps, lock):
    global total_stack

    for _ in range(laps):
        sleep(time)
        lock.acquire()
        total_stack += amount
        lock.release()

def maxstack(lock, thread1, thread2):
    global total_stack

    while thread1.is_alive() or thread2.is_alive():
        sleep(0.1)
        if total_stack >= 11:
            lock.acquire()
            total_stack -= 4
            lock.release()


total_stack = 0
lock = td.Lock()

robot1 = td.Thread(target = stack, args= [0.2, 2, 10, lock])
robot2 = td.Thread(target = stack, args= (0.3, 1, 13, lock))
robot3 = td.Thread(target = maxstack, args = (lock, robot2, robot1), daemon = True)

robot1.start()
robot2.start()
robot3.start()

for _ in range(10):
    sleep(0.4)
    print(total_stack)

robot1.join()
robot2.join()

print('Final:', total_stack)
print(td.enumerate())
