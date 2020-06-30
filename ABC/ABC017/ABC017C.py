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
    N, M = NMI()
    dungeon = [NLI() for _ in range(N)]
    gems = [0] * (M+2)
    total = 0
    for d in dungeon:
        l, r, s = d
        gems[l] += s
        gems[r+1] -= s
        total += s
    cum = []
    for g in gems:
        if not cum:
            cum.append(g)
        else:
            cum.append(cum[-1] + g)
    print(total - min(cum[1:-1]))


if __name__ == "__main__":
    main()