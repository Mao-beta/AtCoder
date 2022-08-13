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


def main(N, S):
    if N == 2:
        if S == S[::-1]:
            print("Yes")
        else:
            print("No")
        exit()

    S = deque(S)
    # print(S)
    while len(S) > 1:
        top = S.popleft()
        bot = S.pop()
        if top == "B" or bot == "A":
            print("Yes")
            exit()

        if top != bot:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    N = NI()
    S = SI()

    main(N, S)


