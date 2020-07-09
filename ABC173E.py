import sys
import math
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, K = NMI()
    A = NLI()
    U = [[abs(a), a//abs(a)] for a in A if a != 0]
    D = sorted(U, reverse=True)
    U = sorted(U)
    print(D)
    print(U)
    if len(D) < K:
        print(0)
        exit()

    ans_d = [1, 1]
    for i, d in enumerate(D):
        if i > K-1:
            break

        if d[1] > 0:
            ans_d[0], ans_d[1] = ans_d[0] * d[0] % MOD, ans_d[1]
        else:
            ans_d[0], ans_d[1] = ans_d[0], ans_d[1] * d[0]



if __name__ == "__main__":
    main()