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
    A = NLI()

    # D[m] mが存在する回の集合
    D = [set() for _ in range(N+1)]
    for i, a in enumerate(A, start=1):
        k = 0
        now = a
        if a < 0:
            k += (-a) // i
            now += k * i

        while True:
            if now > N or k > M:
                break

            if 0 <= now <= N:
                D[now].add(k)

            now += i
            k += 1


    ans = [0] * (M+1)
    for m in range(N+1):
        for d in D[m]:
            if ans[d] == m:
                ans[d] += 1

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
