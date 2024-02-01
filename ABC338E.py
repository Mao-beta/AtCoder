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
    AB = EI(N)
    AB = [[x-1, y-1] for x, y in AB]
    IDX = [0] * (2*N)
    for i, (a, b) in enumerate(AB):
        IDX[a] = i
        IDX[b] = i
    D = deque()
    S = set()
    for i in range(2*N):
        x = IDX[i]
        if x not in S:
            D.append(x)
            S.add(x)
        else:
            if D[-1] != x:
                print("Yes")
                return
            D.pop()
            S.discard(x)
    print("No")


if __name__ == "__main__":
    main()
