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
    A = deque(NLI())
    ans = []
    D = deque()
    for i in range(1, N+1):
        D.append(i)
        if A and i == A[0]:
            A.popleft()
        else:
            while D:
                ans.append(D.pop())
    while D:
        ans.append(D.pop())

    print(*ans)


if __name__ == "__main__":
    main()
