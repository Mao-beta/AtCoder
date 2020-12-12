import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


# Nの素因数分解を辞書で返す
def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    A, B = NMI()
    if A == B:
        print(1)
        exit()

    primes = defaultdict(int)
    for n in range(B+1, A+1):
        for p, num in list(prime_fact(n).items()):
            primes[p] += num
    ans = 1
    for p, num in list(primes.items()):
        ans = ans * (num+1) % MOD
    print(ans)


if __name__ == "__main__":
    main()
