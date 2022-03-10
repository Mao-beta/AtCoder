import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
            now = 0
            for i in range(n):
                if (case >> i) & 1:
                    now += A_half[i]
            res.append(now)
        res.sort()
        return res

    N = len(A)
    return solve_half(A[:N//2]), solve_half(A[N//2:])


def main():
    N, X = NMI()
    W = [NI() for _ in range(N)]
    A, B = split_and_list(W)
    CA = Counter(A)
    CB = Counter(B)
    ans = 0
    for x, k in CA.items():
        ans += k * CB[X-x]
    print(ans)


if __name__ == "__main__":
    main()
