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


def guchoku(N, _A):
    for S in product("ARC", repeat=N):
        S = S[:] + S[:]
        A = _A[:]
        for i in range(N):
            if "".join(S[i:i+3]) in ["ARC", "CRA"]:
                A[i%N] = 1
                A[(i+1)%N] = 1
        if sum(A) == N:
            return True
    return False


def main(N, A):
    if N % 4 == 0:
        return True
    elif N % 4 == 1 or N % 4 == 3:
        if 1 in A:
            return True
        else:
            return False
    else:
        if A.count(1) <= 1:
            return False
        else:
            X = []
            for i, a in enumerate(A):
                if a:
                    X.append(i)
            for i in range(len(X)):
                if (X[(i+1)%len(X)] - X[i]) % 2:
                    return True
            return False


if __name__ == "__main__":
    N = NI()
    A = NLI()
    ans = main(N, A)
    if ans:
        print("Yes")
    else:
        print("No")
    exit()
    for N in range(3, 8):
        for A in product(list(range(2)), repeat=N):
            A = list(A)
            ans = main(N, A)
            gu = guchoku(N, A)
            assert gu == ans, (N, A, gu, ans)