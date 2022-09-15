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
    N = NI()
    M = 1 << N
    A = NLI()
    ans = [0] * M
    rem = deque(range(M))
    for i in range(N):
        tmp = deque()
        while rem:
            x = rem.popleft()
            y = rem.popleft()
            ans[x] += 1
            ans[y] += 1
            if A[x] > A[y]:
                tmp.append(x)
            else:
                tmp.append(y)
        rem = tmp
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
