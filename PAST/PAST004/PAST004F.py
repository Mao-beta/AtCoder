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


from itertools import groupby


def main():
    N, K = NMI()
    S = [SI() for _ in range(N)]
    C = Counter(S).most_common()

    now = 0
    for k, G in groupby(C, key=lambda x: x[1]):
        G = list(G)
        now += len(G)
        if now >= K:
            if len(G) > 1:
                print("AMBIGUOUS")
            else:
                print(G[0][0])
            exit()


if __name__ == "__main__":
    main()
