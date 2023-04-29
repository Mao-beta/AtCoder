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
    H, W = NMI()
    A = [SI() for _ in range(H)]
    B = [SI() for _ in range(H)]

    def check(sh, sw):
        for h in range(H):
            for w in range(W):
                if A[(sh+h)%H][(sw+w)%W] != B[h][w]:
                    return False
        return True


    for sh in range(H):
        for sw in range(W):
            if check(sh, sw):
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
