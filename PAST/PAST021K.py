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
    A = NLI()
    B = NLI()
    C = NLI()
    D = NLI()
    E = NLI()
    # max(x,y) = 1/2 * (x+y - abs(x-y))
    # Ai+Bj-Ci - abs(Ai+Ci-Bj) = 2Dj + 2Ei
    # Ai-Ci-2Ei + Bj-2Dj = abs(Ai+Ci -Bj)
    # i:fixのもと、
    # Ai+Ci >= Bj なるjの中で -Ci-Ei = Dj-Bj なるj
    # Ai+Ci < Bj なるjの中で Ai-Ei = Dj なるj
    # Bをソートしたときに、そのBに対応するDを求めておく
    # j<idxで、Djが p になるのは何個？
    # j>=idxで、Dj-Bjが q になるのは何個？が高速に分かればよい
    # idxがソートされてればいいので、まず全iについてBのカットオフとなるidxを調べてソート
    ACEI = [[a, c, e, i] for i, (a, c, e) in enumerate(zip(A, C, E))]
    ACEI.sort(key=lambda x: x[0]+x[1])
    BDJ = [[b, d, j] for j, (b, d) in enumerate(zip(B, D))]
    BDJ.sort()
    # print(ACEI)
    # print(BDJ)
    DL = Counter()
    DBR = Counter([d-b for b, d in zip(B, D)])
    ans = [0] * N
    idx = 0
    for a, c, e, i in ACEI:
        while idx < N and BDJ[idx][0] < a+c:
            b, d, j = BDJ[idx]
            DL[d] += 1
            DBR[d-b] -= 1
            idx += 1
        ans[i] = DL[a-e] + DBR[-c-e]
    print(*ans)


if __name__ == "__main__":
    main()
