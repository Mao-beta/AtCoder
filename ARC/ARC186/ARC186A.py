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


def count_rowsum(N, A):
    res = []
    for i in range(0, N**2, N):
        res.append(sum(A[i:i+N]))
    return res

def count_colsum(N, A):
    res = []
    for i in range(N):
        res.append(sum(A[i:N**2:N]))
    return res


def check_fixed(N, L):
    base = list(L[0])
    fixed = [1] * (N**2)
    for l in L[1:]:
        for i, b in enumerate(l):
            if base[i] != b:
                fixed[i] = 0
    return fixed

def guchoku(N):
    D = defaultdict(list)
    for A in product([0, 1], repeat=N**2):
        # print(A)
        rowcol = tuple(count_colsum(N, A) + count_rowsum(N, A))
        # print(rowcol)
        D[rowcol].append(A)
        # print()

    C = Counter()
    for rowcol, L in D.items():
        print(rowcol, L)
        fixed = check_fixed(N, L)
        print(sum(fixed), fixed)
        C[sum(fixed)] += 1

    for f, k in C.items():
        print(f, k)


def main(N, Q, Ks):
    ok = [0] * (N**2+1)
    ok[N**2] = 1
    for h in range(2, N+1):
        for w in range(2, N+1):
            ok[N**2 - h*w] = 1

    # print(ok)

    ok[N**2] = 1
    # print(N**2)
    for r in range(2, N+1):
        # print(f"# {r=}")
        for i in range(N-r+1):
            ok[N**2-r**2 - i*r] = 1
            # print(N**2-r**2 - i*r)

    for K in Ks:
        if (N**2-K) % 4 == 0 or K % 4 == 0 or ok[K]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    N, Q = NMI()
    Ks = [NI() for _ in range(Q)]
    main(N, Q, Ks)


#                                                 [1, 0, 0, 1, 0, 1, 0, 0, 0, 1]
#                            [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
# [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1]