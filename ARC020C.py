import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main99():
    N = NI()
    A = []
    L = []
    K = []
    D = []
    for _ in range(N):
        a, l = SMI()
        A.append(int(a))
        L.append(int(l))
        K.append(len(a) * int(l))
        D.append(len(a))

    B = NI()
    MOD = B

    K.append(0)
    K = K[::-1]
    C = list(accumulate(K))[::-1][1:]

    ans = 0
    for a, l, d, c in zip(A, L, D, C):
        x = a * (pow(10, d*l, MOD) - 1) % MOD\
            * pow(pow(10, d, MOD)-1, MOD-2, MOD) % MOD\
            * pow(10, c, MOD) % MOD
        ans += x
        ans %= MOD
    print(ans)


def main():
    N = NI()
    AL = [SLI() for _ in range(N)]
    B = NI()

    ans = 0

    for i in range(N):
        a, l = AL[i]
        k = len(a)
        a, l = int(a), int(l)

        # D[j]はaを2^j(=1<<j)回繋げたもののmodB
        # 2^30 > 10^9よりj=30以上作っておけばok
        D = [a % B]
        for j in range(1, 32):
            # aを1<<(j-1)回繋げたものを、その桁数ぶん(k<<(j-1)桁)ずらしてさらに足す
            # 123123 -> 123123123123 のとき
            # 123123を10進法で6桁左にずらして、123123を足す
            now = D[j-1] * pow(10, (k<<(j-1)), B) + D[j-1]
            now %= B
            D.append(now)

        # xはaをl回繋げたもののmodB
        x = 0
        for j in range(32):
            if (l >> j) & 1:
                x = x * pow(10, (k<<j), B) + D[j]
                x %= B

        # 今までのansを今回のぶん(k*l桁)左にずらしてさらに足す
        ans = ans * pow(10, k*l, B) + x
        ans %= B

    print(ans)


if __name__ == "__main__":
    main()
