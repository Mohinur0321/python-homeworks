import threading

numb = range(1, 100)
start = 1
end = max(numb)
chunk = 3
every = end // chunk
num = end - (every * (chunk - 1))
results = []
result_lock = threading.Lock()

def is_pri(start, end):
    local_primes = []
    for n in range(start, end):
        if n < 2:
            continue
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            local_primes.append(n)
    with result_lock:
        results.extend(local_primes)

# Create threads
t1 = threading.Thread(target=is_pri, args=(1, num))
t2 = threading.Thread(target=is_pri, args=(num + 1, num + every))
t3 = threading.Thread(target=is_pri, args=(num + every, num + every + every))

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for them to finish
t1.join()
t2.join()
t3.join()

# Print result
print(sorted(results))


import threading

results = {}
lock = threading.Lock()

def count_words(lines):
    local = {}
    for line in lines:
        for word in line.split():
            local[word] = local.get(word, 0) + 1
    with lock:
        for word, count in local.items():
            results[word] = results.get(word, 0) + count

with open('your_file.txt') as f:
    lines = f.readlines()

part1 = lines[:len(lines)//3]
part2 = lines[len(lines)//3:2*len(lines)//3]
part3 = lines[2*len(lines)//3:]

t1 = threading.Thread(target=count_words, args=(part1,))
t2 = threading.Thread(target=count_words, args=(part2,))
t3 = threading.Thread(target=count_words, args=(part3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

for word, count in results.items():
    print(word, count)
