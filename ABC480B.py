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

# ライブラリ https://github.com/Mao-beta/AtCoder


def main():
    N, M = NMI()
    S = [SI() for _ in range(N)]
    T = [SI() for _ in range(M)]
    ans = [0] * N
    for t in T:
        L = []
        ok = False
        for i, s in enumerate(S):
            if len(s) != len(t):
                continue
            if s == t:
                ans[i] += 1
                # print(s)
                ok = True
                break
            c = 0
            for ss, tt in zip(s, t):
                if ss != tt:
                    c += 1
            if c == 1:
                L.append(i)
        if ok:
            continue
        if len(L) == 1:
            ans[L[0]] += 1
            # print(t, L[0])
        else:
            pass
            # print("#", t)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
