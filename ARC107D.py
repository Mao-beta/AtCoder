import sys
import math
from collections import deque
from functools import lru_cache

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]

X = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
ans = 0

def main():
    N, K = NMI()
    K *= 2048

    rec(K, 0, N, ans)
    print(ans)


@lru_cache(maxsize=None)
def rec(p, n, N, ans):
    if p == 0:
        print(p, n, N, ans)
    if n == N and p == 0:
        ans += 1
        return
    if n == N and p != 0:
        return

    for x in X:
        if x > p: continue
        rec(p-x, n+1, N, ans)




if __name__ == "__main__":
    main()
