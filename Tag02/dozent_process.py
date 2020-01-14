import time
from multiprocessing import Process, current_process

def square(n):
    time.sleep(0.01)
    print(current_process().pid)
    print(current_process().name)
    print(n*n)

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]

    # for num in nums:
    #     square(num)
    # print()

    processes = []
    for num in nums:
        process = Process(target = square, args= [num])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
        # process.terminate()

    print('Ende')
