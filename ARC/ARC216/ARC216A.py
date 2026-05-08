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


def guchoku(N, A: str, B: str):
    A = list(A)
    B = list(B)
    steps = dict()
    steps["".join(A)] = 0
    D = deque()
    D.append("".join(A))
    while D:
        s = D.popleft()
        now_step = steps[s]
        now = list(s)
        if now == B:
            return now_step
        for i in range(1, N-1):
            if now[i-1] == now[i+1]:
                now[i] = "1" if now[i] == "0" else "0"
                ns = "".join(now)
                if ns not in steps:
                    steps[ns] = now_step + 1
                    D.append(ns)
                now[i] = "1" if now[i] == "0" else "0"
    return -1


def main():
    N = 7
    for A in product("01", repeat=N):
        A = "".join(A)
        if A[0] == "1":
            continue
        for B in product("01", repeat=N):
            B = "".join(B)
            if A == B:
                continue
            if A[0] != B[0] or A[-1] != B[-1]:
                continue
            gu = guchoku(N, A, B)
            print(A, B, gu)


if __name__ == "__main__":
    main()
