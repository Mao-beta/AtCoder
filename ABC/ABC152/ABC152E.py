import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]



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
    N = NI()
    A = NLI()
    L = {}
    primes_a = {}
    for a in A:
        prime_a = prime_fact(a)
        primes_a[a] = prime_a
        for p, n in prime_a.items():
            L.setdefault(p, 0)
            L[p] = max(L[p], n)
    ans = 0
    l = 1
    for p, n in L.items():
        l = l * pow(p, n, MOD) % MOD

    for i, a in enumerate(A):
        ans += l * pow(a, MOD-2, MOD) % MOD
    print(ans % MOD)



if __name__ == "__main__":
    main()