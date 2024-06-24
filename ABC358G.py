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

def sparse_matrix_max_multiply(A, B):
    n = len(A)
    C = [[-float('inf')] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] != -float('inf'):
                for j in range(n):
                    if B[k][j] != -float('inf'):
                        C[i][j] = max(C[i][j], A[i][k] + B[k][j])
    return C

def matrix_max_power(matrix, power):
    n = len(matrix)
    result = [[-float('inf')] * n for _ in range(n)]
    base = matrix

    # 単位行列を初期化
    for i in range(n):
        result[i][i] = 0

    while power > 0:
        if power % 2 == 1:
            result = sparse_matrix_max_multiply(result, base)
        base = sparse_matrix_max_multiply(base, base)
        power //= 2

    return result

def max_weight_walk_bipartite_graph(n1, n2, edges, weights, K):
    size = n1 + n2
    adj_matrix = [[-float('inf')] * size for _ in range(size)]

    # 重み付き隣接行列の作成
    for (u, v), w in zip(edges, weights):
        adj_matrix[u - 1][v - 1] = w
        adj_matrix[v - 1][u - 1] = w

    # 隣接行列の累乗
    max_walk_matrix = matrix_max_power(adj_matrix, K)

    # 長さKのウォークの最大重みを計算
    max_weight = max(max(max_walk_matrix[i]) for i in range(size))

    return max_weight


def main():
    n1 = 3
    n2 = 3
    edges = [(1, 4), (2, 5), (3, 6), (1, 5)]
    weights = [10, 20, 30, 40]
    K = 5
    print(max_weight_walk_bipartite_graph(n1, n2, edges, weights, K))  # 出力例：最大ウォーク重み


if __name__ == "__main__":
    main()
