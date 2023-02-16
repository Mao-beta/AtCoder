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


# 正方行列の積 mod
def mul_matrix(A, B, mod=10**9+7):
    size = len(A)
    ans = [[0] * size for _ in range(size)]
    for h in range(size):
        for w in range(size):
            for i in range(size):
                ans[h][w] += A[h][i] * B[i][w] % mod
                ans[h][w] %= mod
    return ans

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=10**9+7):
    if n == 1:
        size = len(A)
        E = [[0] * size for _ in range(size)]
        for i in range(size):
            E[i][i] = 1
        return mul_matrix(A, E, mod)

    if n % 2 == 0:
        tA = pow_matrix(A, n//2, mod)
        return mul_matrix(tA, tA, mod)
    else:
        tA = pow_matrix(A, n-1, mod)
        return mul_matrix(tA, A, mod)


def main():
    H, W = NMI()
    B = 1<<H
    A = [[0]*B for _ in range(B)]
    
    def dfs(start, state, h):
        if h > H:
            return 
        
        if h == H:
            A[start][state] += 1
            return 
        
        if (start >> h) & 1 == 0:
            ns = state | (1<<h)
            dfs(start, ns, h+1)
        else:
            # 置かない
            ns = state
            dfs(start, ns, h+1)
            # 1x1
            ns = state | (1<<h)
            dfs(start, ns, h+1)
            
            if (start >> (h+1)) & 1:
                # 2x1縦
                ns = state | (1<<h) | (1<<(h+1))
                dfs(start, ns, h+2)
    
    for start in range(B):
        dfs(start, 0, 0)

    P = pow_matrix(A, W, MOD99)
    print(P[-1][-1])


if __name__ == "__main__":
    main()
