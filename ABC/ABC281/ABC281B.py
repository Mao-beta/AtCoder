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
    S = SI()
    E = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if len(S) != 8:
        print("No")
        exit()

    if S[0] not in E or S[-1] not in E:
        print("No")
        exit()

    try:
        N = int(S[1:-1])
        if 100000 <= N <= 999999:
            print("Yes")
        else:
            print("No")

    except:
        print("No")


if __name__ == "__main__":
    main()
