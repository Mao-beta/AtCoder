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
    S = NLI()
    S.sort(reverse=True)
    T = [S[0]]

    for i in range(N):
        tmp = []
        for t in range(1<<i):
            idx = len(T) + t
            if S[idx] < T[t]:
                tmp.append(S[idx])
            else:
                print("No")
                exit()
        T += tmp
    print("Yes")


if __name__ == "__main__":
    main()
