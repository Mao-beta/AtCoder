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
    S = SI()
    X = NI()
    cnt = [0]
    for s in S:
        if "1" <= s <= "9":
            cnt.append(cnt[-1] * (int(s) + 1))
        else:
            cnt.append(cnt[-1] + 1)
        if cnt[-1] > 10**15:
            cnt[-1] = 10**15

    for i in range(len(S), -1, -1):
        if cnt[i] >= X:
            continue
        s = S[i]
        if "1" <= s <= "9":
            X = (X-1) % cnt[i] + 1
        else:
            print(s)
            exit()


if __name__ == "__main__":
    main()
