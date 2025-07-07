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
    H, W = NMI()
    A = EI(H)
    ans = []

    def dfs(case, hw):
        if hw == H*W:
            res = 0
            for i in range(H*W):
                if (case >> i) & 1 == 0:
                    res ^= A[i//W][i%W]
            ans.append(res)
            # print(case, hw, res)
            return

        h, w = divmod(hw, W)
        dfs(case, hw+1)
        if w < W-1:
            if (case >> hw) & 1 == 0 and (case >> (hw+1)) & 1 == 0:
                dfs(case | (1 << hw) | (1 << (hw+1)), hw+2)
        if h < H-1:
            if (case >> hw) & 1 == 0 and (case >> (hw + W)) & 1 == 0:
                dfs(case | (1 << hw) | (1 << (hw+W)), hw+1)

    dfs(0, 0)
    print(max(ans))


if __name__ == "__main__":
    main()
