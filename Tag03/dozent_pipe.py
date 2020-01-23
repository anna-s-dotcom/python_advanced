from multiprocessing import Process, Pipe
from time import sleep

def pipe_connection(conn):
    lis = [42, None, True, 'Hello World!']

    for i in lis:
        conn.send(i)
        if conn.poll():
            print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe(duplex = True)

    p = Process(target = pipe_connection, args = (child_conn, ))

    parent_conn.send('Hallo')
    p.start()

    p.join()
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.poll())
