import time
import threading
from concurrent.futures import ThreadPoolExecutor

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


pool = ThreadPoolExecutor(max_workers=20)

if __name__ == "__main__":
    print("sum:{}".format(sum))
    
    futures = [pool.submit(task_sync, i) for i in range(10)]

    for f in futures:
        f.result()
    
    print("sum:{}".format(sum))