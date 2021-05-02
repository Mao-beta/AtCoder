import sys
import math
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    A = sorted(NLI())
    X = [pow(2, -i, MOD) * a % MOD for i, a in enumerate(A)]
    Y = [pow(2, j-1, MOD) * a % MOD for j, a in enumerate(A)]
    AA = [pow(a, 2, MOD) for a in A]

    sumY = sum(Y) % MOD
    cumY = accumulate(Y)
    ans = 0
    for x, cy in zip(X, cumY):
        ans += x * ((sumY - cy) % MOD)
        ans %= MOD

    ans = (ans + sum(AA)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
