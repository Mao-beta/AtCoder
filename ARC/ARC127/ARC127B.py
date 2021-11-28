import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def to_3(x):
    res = ""
    while x > 0:
        res += str(x%3)
        x //= 3

    return res[::-1]


def main():
    N, L = NMI()
    m = -1
    for i in range(L+5):
        if N <= 3**i:
            m = i
            break

    ans = [[0]*L for _ in range(3*N)]
    for h in range(3*N):
        ans[h][0] = h//N

    for i in range(N):
        x = to_3(i).zfill(m)
        h = 2*N + i
        for w in range(-1, -m-1, -1):
            p = int(x[w])
            ans[h][w] = p
            ans[h-N][w] = (p+1)%3
            ans[h-2*N][w] = (p+2) % 3

    for h in range(N):
        for w in range(1, L-m):
            ans[h][w] = 2
            ans[h+N][w] = 1

    for a in ans:
        print(*a, sep="")


if __name__ == "__main__":
    main()
