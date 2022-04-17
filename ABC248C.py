import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M, K = NMI()
    F = [0] * (K+1)
    F[0] = 1
    G = [1] * (M+1)
    G[0] = 0

    def mul(f, g):
        res = [0] * (len(f))
        for i, ff in enumerate(f):
            for j, gg in enumerate(g):
                if i+j >= len(f):
                    continue
                res[i+j] += ff * gg
                res[i+j] %= MOD
        return res

    for i in range(N):
        F = mul(F, G)

    print(sum(F) % MOD)


if __name__ == "__main__":
    main()
