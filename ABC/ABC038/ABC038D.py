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


def main():
    N = NI()
    size = []
    for i in range(N):
        size.append(NLI())
    size = sorted(size, key=lambda x: x[0])
    H = [s[1] for s in size]
    print(syakutori(H))


# 狭義単調増加列の最長
def syakutori(array):
    n = len(array)
    r = 1
    res = 0
    for l in range(n):
        while 0 < r < n and (r <= l or array[r] > array[r-1]):
            r += 1
        res = max(res, r-l)
        if l == r:
            r += 1

    return res


if __name__ == "__main__":
    main()