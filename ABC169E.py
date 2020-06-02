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
    A = []
    B = []
    for i in range(N):
        a, b = NMI()
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()

    if N%2:
        l = A[(N+1)//2-1]
        r = B[(N+1)//2-1]
        print(r-l+1)
        exit()

    ll = A[N//2-1]
    lr = A[N//2]
    rl = B[N//2-1]
    rr = B[N//2]
    l = (ll+lr)/2
    r = (rl+rr)/2
    gap = r-l
    print(int(gap*2+1))



if __name__ == "__main__":
    main()