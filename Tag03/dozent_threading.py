import threading as td
from time import sleep

def thread_func():
    sleep(0.5)
    print(td.current_thread().name)
    print(td.enumerate())


print(td.current_thread().name)

for i in range(5):
    t = td.Thread(target = thread_func)
    t.start()
    print('count:', td.active_count() )

for t in td.enumerate()[1:]:
    print(t.ident)
    t.join()

print('count:', td.active_count() )
