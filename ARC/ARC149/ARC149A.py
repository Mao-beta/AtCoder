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


def main():
    N, M = NMI()
    ans = [0] * 10
    for x in range(1, 10):
        now = x % M
        for i in range(1, N+1):
            if now == 0:
                ans[x] = i
            now = now * 10 + x
            now %= M

    ans = [(ans[i], i) for i in range(1, 10)]
    ans.sort(key=lambda x: (-x[0], -x[1]))
    k, x = ans[0]
    if k > 0:
        print(str(x) * k)
    else:
        print(-1)


if __name__ == "__main__":
    main()
