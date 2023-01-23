import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def query(i, j, k):
    print(f"? {i} {j} {k}", flush=True)
    res = SI()
    assert res != "-1"
    return res == "Yes"


def answer(P):
    P = ["!"] + P
    print(*P, flush=True)


def main():
    N = NI()

    if N == 1:
        answer([1])
        exit()

    # 1を探す
    # Pi + Pi > Pk がFalseならkを更新
    k = 1
    for i in range(2, N+1):
        res = query(i, i, k)
        if not res:
            k = i

    ONE = k

    # i != k において Pi + 1 > Pk は Pi > Pk と同値
    # これを利用してマージソート
    D = deque()
    for i in range(1, N+1):
        D.append(deque([i]))

    while len(D) > 1:
        X = D.popleft()
        Y = D.popleft()
        Z = deque()

        while X and Y:
            x = X[0]
            y = Y[0]
            x_is_bigger = query(x, ONE, y)
            if x_is_bigger:
                Z.append(y)
                Y.popleft()
            else:
                Z.append(x)
                X.popleft()

        Z += X + Y
        D.append(Z)

    IDX = D[0]

    P = [0] * N
    for i in range(1, N+1):
        idx = IDX.popleft()
        P[idx-1] = i

    answer(P)


if __name__ == "__main__":
    main()
