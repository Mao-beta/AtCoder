import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    TX = EI(N)
    ans = []
    needs = [0] * (N+1)
    for t, x in TX[::-1]:
        if t == 2:
            needs[x] += 1
        else:
            if needs[x] > 0:
                ans.append(1)
                needs[x] -= 1
            else:
                ans.append(0)

    if sum(needs) > 0:
        print(-1)
        return

    ans = ans[::-1]
    k = 0
    Kmin = 0
    P = [0] * (N+1)
    ai = 0
    for t, x in TX:
        if t == 1:
            if ans[ai]:
                P[x] += 1
                k += 1
            ai += 1
        else:
            P[x] -= 1
            k -= 1
        Kmin = max(Kmin, k)

    print(Kmin)
    print(*ans)


if __name__ == "__main__":
    main()
