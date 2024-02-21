import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, T = SMI()
    N = int(N)
    S = [SI() for _ in range(N)]
    ans = []
    tn = len(T)
    for i, s in enumerate(S):
        sn = len(s)
        if sn < tn-1 or sn > tn+1:
            continue
        if sn == tn:
            bad = 0
            for ss, tt in zip(s, T):
                if ss != tt:
                    bad += 1
            if bad <= 1:
                ans.append(i+1)
        elif sn != tn:
            t = T
            if tn < sn:
                s, t = t, s
            si, ti = 0, 0
            while si < len(s) and ti < len(t):
                if s[si] == t[ti]:
                    si += 1
                    ti += 1
                else:
                    ti += 1
            if si == len(s) and ti >= len(t)-1:
                ans.append(i+1)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
