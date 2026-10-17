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
    X, Y = 0, 0
    A = EI(N)
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                X, Y = i, j
            A[i][j] -= 1
    for i in range(N):
        for j in range(N):
            for k in range(N):
                aij = A[i][j]
                ajk = A[j][k]
                if aij == -1 or ajk == -1:
                    continue
                if A[aij][k] == -1 or A[i][ajk] == -1:
                    continue
                if A[aij][k] != A[i][ajk]:
                    print(ans)
                    return
    for a in range(N):
        A[X][Y] = a
        aij = a
        ok = True
        for k in range(N):
            ajk = A[Y][k]
            if A[aij][k] != A[X][ajk]:
                ok = False
        ajk = a
        for i in range(N):
            aij = A[i][X]
            if A[aij][Y] != A[i][ajk]:
                ok = False

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
