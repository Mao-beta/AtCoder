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
    N, M = NMI()
    LR = EI(M)
    LR = [[x-1, y] for x, y in LR]
    L2Rs = [[] for _ in range(N+1)]
    R2Ls = [[] for _ in range(N+1)]
    for l, r in LR:
        L2Rs[l].append(r)
        R2Ls[r].append(l)
    for i in range(N+1):
        L2Rs[i].sort()
        R2Ls[i].sort()
    rm, rm2 = N+1, N+1
    RMs = [[N+1, N+1] for _ in range(N+2)]
    for i in range(N, -1, -1):
        RMs[i] = RMs[i+1][:]
        Rs = L2Rs[i]
        if len(Rs) == 0:
            continue
        elif len(Rs) == 1:
            if Rs[0] <= rm:
                rm, rm2 = Rs[0], rm
            elif Rs[0] <= rm2:
                rm2 = Rs[0]
        else:
            if Rs[0] <= rm:
                rm, rm2 = Rs[0], rm
            elif Rs[0] <= rm2:
                rm2 = Rs[0]
            if Rs[1] <= rm:
                rm, rm2 = Rs[1], rm
            elif Rs[1] <= rm2:
                rm2 = Rs[1]
        RMs[i] = [rm, rm2]

    # print(L2Rs)
    Q = NI()
    ST = EI(Q)
    ST = [[x-1, y] for x, y in ST]
    for s, t in ST:
        R = L2Rs[s]
        idx = bisect.bisect_right(R, t)
        # print(s, t, R, idx)
        if idx == 0:
            print("No")
            continue
        sr = R[idx-1]
        if sr < t:
            L = R2Ls[t]
            idx = bisect.bisect_left(L, s)
            if idx == len(L):
                print("No")
                continue
            tl = L[idx]
            if tl <= sr:
                print("Yes")
            else:
                print("No")
        else:
            rm, rm2 = RMs[s]
            if rm < t:
                print("Yes")
            elif rm2 == t:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
