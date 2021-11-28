import sys
import math
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = SI()
    N = len(S)
    A = list(map(int, S))
    C = list(accumulate([0]+A))
    pow2 = [1]
    pow10 = [1]
    for i in range(N):
        pow2.append(pow2[-1] * 2 % MOD)
        pow10.append(pow10[-1] * 10 % MOD)

    ans = 0
    for i in range(1, N):
        ans = ans + pow2[i-1] * C[i] % MOD * pow10[N-1-i] % MOD
        ans %= MOD

    for i in range(N):
        ans += pow10[N-1-i] * pow2[i] % MOD * int(S[i]) % MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
