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
EI = lambda m: [tuple(NMI()) for _ in range(m)]


def split_and_list(A):
    """
    半分全列挙
    :param A: 長さ40以下くらいのList
    :return: 前半と後半それぞれについて、各部分集合の和のList
    """

    def solve_half(A_half):
        n = len(A_half)
        res = []
        for case in range(1<<n):
            now_v = 0
            now_w = 0
            for i in range(n):
                if (case >> i) & 1:
                    now_v += A_half[i][0]
                    now_w += A_half[i][1]
            res.append(now_w * 10**22 + now_v)
        res.sort()
        return res

    N = len(A)
    return solve_half(A[:N//2]), solve_half(A[N//2:])


def main():
    N, W = NMI()
    VW = EI(N)
    A, B = split_and_list(VW)
    A.sort()
    B.sort()
    Ws = [0]
    Vs = [0]
    for wv in B[1:]:
        w, v = divmod(wv, 10**22)
        Ws.append(w)
        Vs.append(max(Vs[-1], v))

    ans = 0
    idx = len(B)
    for wv in A:
        w, v = divmod(wv, 10 ** 22)
        bw = W - w
        if bw < 0:
            break
        while idx > 1 and Ws[idx-1] > bw:
            idx -= 1
        ans = max(ans, Vs[idx-1] + v)

    print(ans)


if __name__ == "__main__":
    main()
