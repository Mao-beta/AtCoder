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
    H, W = NMI()
    S = [list(SI()) for _ in range(H)]
    if W > H:
        H, W = W, H
        S = [x for x in zip(*S)]
    dp = defaultdict(int)
    dp["#"*W] = 1
    for h in range(H):
        for w in range(W):
            dp2 = defaultdict(int)
            s = S[h][w]
            if s == "?":
                for ns in "123":
                    for key, val in dp.items():
                        if w > 0:
                            if key[0] == ns or key[-1] == ns:
                                continue
                        else:
                            if key[0] == ns:
                                continue
                        nkey = key[1:] + ns
                        dp2[nkey] += val
                        dp2[nkey] %= MOD99
            else:
                ns = s
                for key, val in dp.items():
                    if w > 0:
                        if key[0] == ns or key[-1] == ns:
                            continue
                    else:
                        if key[0] == ns:
                            continue
                    nkey = key[1:] + ns
                    dp2[nkey] += val
                    dp2[nkey] %= MOD99
            dp = dp2
    print(sum(dp.values()) % MOD99)


if __name__ == "__main__":
    main()
