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


def main():
    N = NI()
    Pre = NLI()
    In = NLI()

    def reconstruct_post_from_pre_and_in(Pre, In):
        """
        PreorderとInorderの列からPostorderを復元する
        """
        In_inv = {x: i for i, x in enumerate(In)}
        now = [0]
        ans = []

        def rec(l, r):
            if l >= r: return
            root = Pre[now[0]]
            now[0] += 1
            idx = In_inv[root]
            rec(l, idx)
            rec(idx+1, r)
            ans.append(root)

        rec(0, N)
        return ans

    print(*reconstruct_post_from_pre_and_in(Pre, In))


if __name__ == "__main__":
    main()
