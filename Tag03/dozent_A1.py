# Nutze threading.Thread

# Erstelle zwei "Roboter" (je als Thread), die Kisten Stapeln.
# Der erste stapelt alle 0.2 Sekunden 2 Kisten, der zweite Stapelt alle 0.3 Sekunden 1 Kiste. Der erste macht 10 Durchläufe, der zweite macht 13 Durchläufe.

# Lasse die Roboter alle Kisten stapeln und dir die Anzahl der Kisten auf dem Stapel ausgeben.

from time import sleep
import threading as td

def stack(time, amount, laps, lock):
    global total_stack

    for _ in range(laps):
        sleep(time)
        lock.acquire()
        total_stack += amount
        lock.release()

total_stack = 0
lock = td.Lock()

robot1 = td.Thread(target = stack, args= [0.2, 2, 10, lock])
robot2 = td.Thread(target = stack, args= (0.3, 1, 13, lock))

robot1.start()
robot2.start()

for _ in range(10):
    sleep(0.4)
    print(total_stack)

robot1.join()
robot2.join()

print('Final:', total_stack)
