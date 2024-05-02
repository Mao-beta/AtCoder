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
    D = deque()
    # 反転ありか
    Cap = [0] * N
    # カッコ列の相方
    P = [-1] * N
    for i, s in enumerate(S):
        if s == "(":
            D.append(i)
        elif s == ")":
            p = D.pop()
            P[p] = i
            P[i] = p
        else:
            Cap[i] = len(D) % 2

    seen = [0] * N
    order = []

    def rec(now, d):
        while 0 <= now < N:
            s = S[now]
            if seen[now]:
                return
            seen[now] = 1
            order.append(now)
            if d == 1:
                if s == "(":
                    rec(P[now]-1, -1)
                    now = P[now]+1
                elif s == ")":
                    seen[now] = 1
                    return
                else:
                    now += d
            else:
                if s == "(":
                    seen[now] = 1
                    return
                elif s == ")":
                    rec(P[now]+1, 1)
                    now = P[now]-1
                else:
                    now += d

    rec(0, 1)

    ans = []
    for idx in order:
        s = S[idx]
        if s in "()":
            continue
        if Cap[idx]:
            if s.isupper():
                ans.append(s.lower())
            else:
                ans.append(s.upper())
        else:
            ans.append(s)

    print("".join(ans))


if __name__ == "__main__":
    main()
