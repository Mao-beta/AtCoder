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
    N = NI()
    res = [0] * N
    t = 0
    now = 0
    for i in range(1, N):
        print(f"? 1 {i+1}", flush=True)
        X = NI()
        if X > now:
            t = i
            now = X
    # P[t]は右端か左端
    for i in range(N):
        if t == i:
            continue
        print(f"? {t+1} {i+1}", flush=True)
        X = NI()
        res[i] = X
    # res[i]はP[t]からP[i]の区間和
    # P[t]をとりあえず左端とする
    RI = [[r, i] for i, r in enumerate(res)]
    RI.sort()
    # print(RI)
    # RIのidx=P[i]、左からの累積和とクエリの番号
    # [0, t], [X_pi, i], ...
    P = [0] * N
    A = [0] * N
    for idx, (xp, i) in enumerate(RI):
        P[i] = idx
        if idx >= 2:
            A[idx] = RI[idx][0] - RI[idx-1][0]

    print(f"? {RI[1][1]+1} {RI[-1][1]+1}", flush=True)
    X = NI()
    A[0] = RI[-1][0] - X
    A[1] = RI[1][0] - A[0]
    # print(f"{A=}")
    # print(f"{P=}")
    if P[0] > P[1]:
        A = A[::-1]
        P = [N-1-p for p in P]
    P = [x+1 for x in P]
    print(f"! {' '.join(map(str, P))} {' '.join(map(str, A))}", flush=True)


if __name__ == "__main__":
    main()
