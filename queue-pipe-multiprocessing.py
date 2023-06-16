import multiprocessing

### Sharing memory using array & values between parent process and p1 ###
result = []

def calc_square(numbers, v):
    global result
    for idx, n in enumerate(numbers):
        # result.append(n*n)
        result[idx] = n*n
    print('inside process ' + str(result))

numbers = [2,3,5,6,7,8]

result = multiprocessing.Array('i',6)
v = multiprocessing.Value('d',0.0)

p1 = multiprocessing.Process(target=calc_square, args=(numbers,v))

p1.start()
p1.join()

# print('Ouside Process' + str(result))
print(result[:])
print(v.value)


### Sharing memory using Queue (Shared Memory) ###

def queue_calc_square(numbers, q):
    for n in numbers:
        q.put(n*n) # for Queue

q = multiprocessing.Queue()

p2 = multiprocessing.Process(target=queue_calc_square, args=(numbers,q))

p2.start()
p2.join()

while q.empty() is False:
    print(q.get())