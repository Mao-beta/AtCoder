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


def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    N = NI()
    L = list(prime_fact(N).values())
    ans = 0
    for l in L:
        if 1 <= l < 3:
            ans += 1
        elif 3 <= l < 6:
            ans += 2
        elif 6 <= l < 10:
            ans += 3
        elif 10 <= l < 15:
            ans += 4
        elif 15 <= l < 21:
            ans += 5
        elif 21 <= l < 28:
            ans += 6
        elif 28 <= l < 36:
            ans += 7
        elif 36 <= l:
            ans += 8
    print(ans)


if __name__ == "__main__":
    main()