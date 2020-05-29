import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]

#隣接リスト 1-order
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res

def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


def pow_mod(base, exp, m):
    if exp == 1:
        return base % m
    elif exp % 2:
        return pow_mod(base, exp-1, m) * base % m
    else:
        return pow_mod(base, exp//2, m) ** 2 % m


def main():
    edges = [[2, 3], [3, 1], [4, 1]]
    N = make_adjlist_d(5, edges)
    print(N)
    N = make_adjlist_nond(5, edges)
    print(cmb(1000, 500) % MOD)
    pass


if __name__ == "__main__":
    main()