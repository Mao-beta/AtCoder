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
    A = NLI()
    A = sorted(A)

    hurui = [0] * (10**7)
    prev = 0
    ex = set()
    for a in A:
        hurui[a] = 1
        if prev == a:
            ex.add(a)
        prev = a
    for i in range(1010):
        if hurui[i] == 0:
            continue
        j = 2
        while j * i <= 10**6 + 100:
            hurui[i*j] = 0
            j += 1

    print(sum(hurui) - len(ex))



if __name__ == "__main__":
    main()