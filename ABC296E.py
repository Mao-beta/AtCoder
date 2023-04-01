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
    N = NI()
    A = NLI()
    A = [x-1 for x in A]
    D = [0] * N
    for i, a in enumerate(A):
        D[a] += 1

    que = deque()
    for i, d in enumerate(D):
        if d == 0:
            que.append(i)

    bad = set()
    while que:
        now = que.popleft()
        bad.add(now)
        D[A[now]] -= 1
        if D[A[now]] == 0:
            que.append(A[now])
    print(N - len(bad))


if __name__ == "__main__":
    main()
