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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    t, N = NMI()
    K = 100
    ok = [0] * ((100+t)*K//100)
    for i in range(K):
        x = (100+t) * i // 100
        ok[x] = 1
    # print(len(ok), sum(ok))
    bad = len(ok) - sum(ok)
    bad_X = [i for i, x in enumerate(ok) if x == 0]
    p, q = divmod(N-1, bad)
    ans = p * len(ok) + bad_X[q]
    # print(p, q)
    print(ans)


if __name__ == "__main__":
    main()
