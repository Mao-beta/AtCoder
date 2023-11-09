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
    FS = EI(N)
    FS.sort(key=lambda x: -x[1])
    ans = 0
    for i in range(1, N):
        f, s = FS[i]
        if f == FS[0][0]:
            res = FS[0][1] + s // 2
        else:
            res = FS[0][1] + s
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
