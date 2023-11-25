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

    if N == 3:
        print(1, 3, 2, 3, 2, 3)
        exit()

    D = deque()

    if N % 2:
        for x in range(1, N-3+1):
            if x % 2:
                D.append(x)
            else:
                D.appendleft(x)
    else:
        for x in range(1, N-3+1):
            if x % 2:
                D.appendleft(x)
            else:
                D.append(x)

    # print(D)
    ans = []
    for i in range(N-2):
        ans.append(N-2)
        ans.append(N)
        ans.append(N-1)
        for d in D:
            if d > i:
                ans.append(d)


    ans.append(N)
    ans.append(N-1)
    ans.append(N)

    # print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
