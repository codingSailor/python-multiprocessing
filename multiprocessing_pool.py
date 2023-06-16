from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(10000):
        sum += x*x
    return sum

t1 = time.time()
p = Pool(processes=3)
result = p.map(f, range(10000))
p.close()
p.join()

print("Pool took: ", time.time()- t1)

result = []
t2 = time.time()
for x in range(10000):
        result.append(f(x))

print("Serial processing took: ", time.time()- t2)

