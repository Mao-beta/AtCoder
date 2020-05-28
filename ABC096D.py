N = int(input())

primes = [1] * (55555+1)
primes[0] = 0
primes[1] = 0
for i in range(len(primes)):
    if primes[i] == 0: continue
    pi = i*2
    while pi <= 55555:
        primes[pi] = 0
        pi += i

ans = []
for i, p in enumerate(primes):
    if i % 5 == 1 and p:
        ans.append(i)

print(" ".join(map(str, ans[0:N])))