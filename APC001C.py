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
    N = int(input())

    def query(i):
        print(i)
        sys.stdout.flush()
        q = input()
        if q == "Vacant":
            exit()
        return q[0]

    if N <= 20:
        for i in range(N):
            query(i)

    def judge(l, r):
        d = r - l - 1
        if ans[l % N] == ans[r % N] and d % 2 == 0:
            return True
        elif ans[l % N] != ans[r % N] and d % 2 == 1:
            return True
        else:
            return False

    ans = [""] * N
    ans[0] = query(0)
    ans[N // 2] = query(N // 2)
    if judge(0, N // 2):
        l, r = 0, N // 2
    else:
        l, r = N // 2, N

    for i in range(19):
        m = (l + r) // 2
        res = query(m)
        ans[m] = res
        if judge(l, m):
            r = m
        else:
            l = m


if __name__ == "__main__":
    main()
