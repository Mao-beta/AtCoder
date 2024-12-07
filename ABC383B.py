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
    H, W, D = NMI()
    S = [SI() for _ in range(H)]
    ans = 0
    for hw1 in range(H*W):
        for hw2 in range(hw1+1, H*W):
            h1, w1 = divmod(hw1, W)
            h2, w2 = divmod(hw2, W)
            if S[h1][w1] == "#" or S[h2][w2] == "#":
                continue
            tmp = 0
            for hw in range(H*W):
                h, w = divmod(hw, W)
                if S[h][w] == "#":
                    continue
                if abs(h1-h) + abs(w1-w) <= D or abs(h2-h) + abs(w2-w) <= D:
                    tmp += 1
            ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
