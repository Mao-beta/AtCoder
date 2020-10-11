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


def main():
    T = NI()
    case = [NLI() for _ in range(T)]

    for N, A, B in case:
        A, B = max(A, B), min(A, B)
        ans = (N-A+1)**2 * (N-B+1)**2 % MOD

        #内部
        ans = (ans - (A-B+1)**2 * (N-A+1)**2) % MOD

        #辺
        kx = min(B-1, N-A+1)
        m = 2 * (A-B+1) * (N-A+1) * kx * (2*N - 2*A - kx + 1) % MOD
        ans = (ans - m) % MOD

        # 頂点
        kx = max(1, A+B-N-1)
        ky = max(1, A+B-N-1)
        m = (B-1)**2 * (B-kx)**2 * (2*N - 2*A - B + kx + 1)**2 % MOD
        ans = (ans - m) % MOD

        print(ans)




if __name__ == "__main__":
    main()
