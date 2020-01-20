import queue

print('start fifo')

fifoq = queue.Queue()

fifoq.put(5)
fifoq.put('A')
fifoq.put(True)
fifoq.put([1, 5])

while not fifoq.empty():
    print(fifoq.get())

print()
print('end fifo')
print()

print('start lifo')

lifoq = queue.LifoQueue()

lifoq.put(5)
lifoq.put('A')
lifoq.put(True)
lifoq.put([1, 5])

while not lifoq.empty():
    print(lifoq.get())

print()
print('end lifo')
print()

print('start prio')

prioq = queue.PriorityQueue()

prioq.put((1, 'XX'))
prioq.put((5, 'A'))
prioq.put((3, True))
prioq.put((2, [1, 5]))
prioq.put((1, 'B'))

while not prioq.empty():
    print(prioq.get())

print()
print('end prio')
print()
