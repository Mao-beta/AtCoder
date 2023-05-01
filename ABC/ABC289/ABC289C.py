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
    N, M = NMI()
    A = []
    for _ in range(M):
        c = NI()
        A.append(set(NMI()))

    ans = 0
    for case in range(1<<M):
        ok = [False] * N
        for x in range(N):
            for i in range(M):
                if (case >> i) & 1:
                    if x+1 in A[i]:
                        ok[x] = True
                        break

        if all(ok):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
