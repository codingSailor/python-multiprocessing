import time
import multiprocessing

### Inconsistency before using lock ###

def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1

def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1

balance = multiprocessing.Value('i', 200)
d = multiprocessing.Process(target=deposit, args=(balance,))
w = multiprocessing.Process(target=withdraw, args=(balance,))

d.start()
w.start()
d.join()
w.join()
print("Before Lock", balance.value)


### Consistency after using lock ###

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

balance = multiprocessing.Value('i', 200)
lock = multiprocessing.Lock()
d = multiprocessing.Process(target=deposit, args=(balance,lock))
w = multiprocessing.Process(target=withdraw, args=(balance,lock))

d.start()
w.start()
d.join()
w.join()
print("After Applying Lock", balance.value)