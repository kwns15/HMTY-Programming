memo = [1,1]

def fib(n):
    global memo
    if len(memo) > n:
        return memo[n - 1]
    else:
        for i in range(len(memo), n):
            memo.append(memo[i-1] + memo[i-2])
        return memo[-1]

primes = [2,3]

def isprime(x):
    for i in range(2,int(x ** 0.5 + 1)):
        if x % i == 0 : return False
    return True

def nprime(n):
    if len(primes) > n:
        return primes[n-1]
    else:
        while len(primes) < n:
            i = primes[-1] + 1
            while not isprime(i):
                i += 1
            primes.append(i)
        return primes[-1]
            
###Θεμα 1
while True:
    num = input()

    if num == 'END':
        break
    num = int(num)
    print(fib(num))

'''
## Θεμα 2
while True:
    num = input()

    if num == 'END':
        break
    num = int(num)
    print(nprime(num))

## Θεμα 3
j = 3


for i in range(10):
    n = fib(j)
    while not isprime(n):
        j += 1
        n = fib(j)
    j += 1
    print(n)

#θεμα 4

n = 1       
for i in range(2):
    while True:
        if fib(n) % nprime(n) == 0: break
        n +=1 
    print(n)
    n += 1
'''
