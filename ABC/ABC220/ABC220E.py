import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, D = NMI()
    ans = 0

    if 2*(N-1) < D:
        print(ans)
        exit()

    for k in range(D+1):
        left = k
        right = D - k
        if left > N-1 or right > N-1:
            continue

        if k < D/2:
            base = pow(2, N-D+k, MOD) - 1
        else:
            base = pow(2, N-k, MOD) - 1

        if k == 0 or k == D:
            ans += pow(2, D-1, MOD) * base % MOD
        else:
            ans += pow(2, D-2, MOD) * base % MOD

        ans %= MOD

    print(ans*2%MOD)


if __name__ == "__main__":
    main()
