import sys
import math
from math import gcd
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    LA = [1] * N
    RA = [1] * N
    for i in range(N):
        if i == 0:
            LA[0] = A[0]
            RA[N-1] = A[N-1]
            continue
        LA[i] = gcd(LA[i-1], A[i])
        RA[N-i-1] = gcd(RA[N-i], A[N-i-1])
    ans = 0
    for i in range(N):
        if i == 0:
            ans = RA[1]
            continue
        if i == N-1:
            ans = max(ans, LA[N-2])
            continue
        ans = max(ans, gcd(LA[i-1], RA[i+1]))
    print(ans)


if __name__ == "__main__":
    main()