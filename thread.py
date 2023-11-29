import time
import threading

sum = 0
lock = threading.Lock()

def task_sync(s=0):
    print("sync task:{0} begin, thread:{1}".format(s, threading.current_thread().name))

    global sum
    lock.acquire()
    sum += 1
    lock.release()

    time.sleep(1)
    print("sync task:{0} complete, thread:{1}".format(s, threading.current_thread().name))


if __name__ == "__main__":
    print("sum:{}".format(sum))

    ts = [threading.Thread(target=task_sync, args=(i,)) for i in range(10)]

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    print("sum:{}".format(sum))
