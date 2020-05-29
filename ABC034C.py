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
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def cmb_mod(n, r, m):
    fact = [1] * (n+1)
    inv = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] *= fact[i-1] * i % m
        inv[i] *= inv[i-1] * pow(i, m-2, m) % m
    return fact[n] * inv[r] * inv[n-r] % m




def main():
    W, H = NMI()
    print(cmb_mod(W+H-2, W-1, MOD))


if __name__ == "__main__":
    main()