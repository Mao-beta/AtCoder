import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N = len(S)
    B = 1 << N
    ans = 0
    for case in range(1, B-1):
        X = []
        Y = []
        for i in range(N):
            if (case >> i) & 1:
                X.append(S[i])
            else:
                Y.append(S[i])
        X.sort(reverse=True)
        Y.sort(reverse=True)
        if len(X) == 0 or len(Y) == 0 or X[0] == "0" or Y == "0":
            continue
        ans = max(ans, int("".join(X)) * int("".join(Y)))
    print(ans)


if __name__ == "__main__":
    main()
