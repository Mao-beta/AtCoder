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
    N, M, L = NMI()
    A = NLI()
    B = NLI()
    C = NLI()
    memo = defaultdict(bool)

    def dfs(player):
        # player0: takahashi
        # print(A, B, C, player)
        key = str(sorted(list(A))) + str(sorted(list(B))) + str(sorted(list(C))) + str(player)
        if key in memo:
            return memo[key]

        # print(key)
        res = False
        if player == 0:
            X = A
        else:
            X = B

        if len(X) == 0:
            memo[key] = res
            return res
        for a in list(X):
            if res:
                break
            X.remove(a)
            C.append(a)
            if not dfs(player ^ 1):
                res = True

            for c in list(C):
                if res:
                    break
                if c < a:
                    C.remove(c)
                    X.append(c)
                    if not dfs(player^1):
                        res = True
                    X.remove(c)
                    C.append(c)

            C.remove(a)
            X.append(a)

        memo[key] = res
        # print(key, res)
        return res


    # print(memo.values())

    if dfs(0):
        print("Takahashi")
    else:
        print("Aoki")



if __name__ == "__main__":
    main()
