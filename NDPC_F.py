import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


from collections import deque

class CartesianTree:
    def __init__(self, P):
        # 順列 P についてCartesianTreeを構築 O(N)
        N = len(P)
        self.N = N
        self.P = P[:]
        D = deque()
        self.root = 0
        self.left = [-1] * N
        self.right = [-1] * N
        self.par = [-1] * N

        for i, p in enumerate(P):
            last = -1
            while D and P[D[-1]] > p:
                last = D.pop()
            if last != -1:
                self.left[i] = last
                self.par[last] = i
            if D:
                self.right[D[-1]] = i
                self.par[i] = D[-1]
            D.append(i)

        for i in range(N):
            if self.par[i] == -1:
                self.root = i
                break

    def dfs(self, A):
        stack = deque()
        stack.append(~self.root)
        stack.append(self.root)

        # 頂点iの部分木以下でサイズjの最小コスト
        INF = 10**16
        dps = [[] for _ in range(self.N)]

        while stack:
            v = stack.pop()
            if v >= 0:
                l, r = self.left[v], self.right[v]
                if l != -1:
                    stack.append(~l)
                    stack.append(l)
                if r != -1:
                    stack.append(~r)
                    stack.append(r)

            else:
                v = ~v
                l, r = self.left[v], self.right[v]
                dpl = dps[l] if l != -1 else [0]
                dpr = dps[r] if r != -1 else [0]
                dp = [INF] * (len(dpl) + len(dpr))
                # 左だけ
                for k, d in enumerate(dpl):
                    dp[k] = min(dp[k], d)
                # 右だけ
                for k, d in enumerate(dpr):
                    dp[k] = min(dp[k], d)
                # 両方使うときはvも使う
                for kl, dl in enumerate(dpl):
                    if dl >= INF:
                        continue
                    for kr, dr in enumerate(dpr):
                        if dr >= INF:
                            continue
                        dp[kl+kr+1] = min(dp[kl+kr+1], dl + dr + A[v])

                dps[v] = dp

        return dps[self.root]

    def __str__(self):
        return f"{self.root=}\n{self.left=}\n{self.right=}\n{self.par=}"


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        P = NLI()
        A = NLI()
        tree = CartesianTree(P)
        dp = tree.dfs(A)
        print(*dp[1:])



if __name__ == "__main__":
    main()
