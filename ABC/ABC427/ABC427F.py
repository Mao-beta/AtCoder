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
    A = NLI()

    # if N == 1:
    #     if A[0] == M:
    #         print(2)
    #     else:
    #         print(1)
    #     return

    X = A[:N//2]
    Y = A[N//2:]


    def preprocess(Z):
        ZN = len(Z)
        cands = [[] for _ in range(ZN+2)]
        cands[0].append(0)

        for i in range(ZN):
            z = Z[i]
            for c in cands[i]:
                cands[i+1].append(c % M)
                cands[i+2].append((c+z) % M)

        return Counter(cands[-1]), Counter(cands[-2]) # 最後含む、含まない

    PX_l, PX_n = preprocess(X)
    PY_l, PY_n = preprocess(Y[::-1])
    # print(len(PX_l) + len(PX_n) + len(PY_l) + len(PY_n))
    # print(PX_l, PX_n, PY_l, PY_n)

    ans = 0
    for c, k in PX_l.items():
        ans += k * (PY_n[-c] + PY_n[M - c] + PY_n[2 * M - c])
    for c, k in PX_n.items():
        ans += k * (PY_n[-c] + PY_n[M - c] + PY_n[2 * M - c])
        ans += k * (PY_l[-c] + PY_l[M - c] + PY_l[2 * M - c])
    print(ans)


if __name__ == "__main__":
    main()
