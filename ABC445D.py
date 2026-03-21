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
    H, W, N = NMI()
    HW = EI(N)
    H2WI = defaultdict(list)
    W2HI = defaultdict(list)
    ans = [[0, 0] for _ in range(N)]
    for i, (h, w) in enumerate(HW):
        H2WI[h].append((w, i))
        W2HI[w].append((h, i))
    nh, nw = 0, 0
    used = [0] * N
    # print(H2WI)
    # print(W2HI)
    for _ in range(N):
        if H2WI[H]:
            for w, i in H2WI[H]:
                if used[i]:
                    continue
                ans[i] = [nh, nw]
                nw += w
                W -= w
                used[i] = 1
            H2WI[H] = []
        elif W2HI[W]:
            for h, i in W2HI[W]:
                if used[i]:
                    continue
                ans[i] = [nh, nw]
                nh += h
                H -= h
                used[i] = 1
            W2HI[W] = []
        # print(H, W, used)
    for h, w in ans:
        print(h+1, w+1)


if __name__ == "__main__":
    main()
