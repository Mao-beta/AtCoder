import sys
import math
from collections import deque
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    C = [NLI() for _ in range(10)]
    A = [NLI() for _ in range(H)]

    for i in range(10):
        for perm in permutations("0123456789", 3):
            now = int(perm[0])
            cost = 0
            for p in perm[1:]:
                p = int(p)
                cost += C[now][p]
                now = p
            C[int(perm[0])][now] = min(C[int(perm[0])][now], cost)

    ans = 0
    for h in range(H):
        for w in range(W):
            now = A[h][w]
            if now == -1: continue
            ans += C[now][1]
    print(ans)


if __name__ == "__main__":
    main()