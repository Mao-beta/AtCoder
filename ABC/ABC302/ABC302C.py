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
    S = [SI() for _ in range(N)]

    def check(p):
        for i in range(N-1):
            s1, s2 = p[i], p[i+1]
            diff = 0
            for ss1, ss2 in zip(s1, s2):
                if ss1 != ss2:
                    diff += 1

            if diff != 1:
                return False

        return True

    for P in permutations(S):
        if check(P):
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
