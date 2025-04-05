import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, Q = NMI()
    S = SI()
    TD = [SLI() for _ in range(Q)]

    def f(_S, rev=False):
        if rev:
            S = _S[::-1]
        else:
            S = _S[:]

        def judge(X):
            i = X
            s = S[i]
            for t, d in TD:
                if rev:
                    if d == "L":
                        d = "R"
                    else:
                        d = "L"
                if t == s:
                    if d == "L":
                        i -= 1
                    else:
                        i += 1
                    if i < 0:
                        return True
                    if i >= N:
                        return False
                    s = S[i]
            return False

        ok = -1
        ng = N
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X):
                ok = X
            else:
                ng = X

        if rev:
            ok = N - ok - 1
        return ok

    L_ok = f(S)
    R_ok = f(S, rev=True)
    # print(L_ok, R_ok)
    print(N - (L_ok+1) - (N-R_ok))


if __name__ == "__main__":
    main()
