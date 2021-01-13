import sys
import math
from collections import defaultdict
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
    C = NLI()
    C.sort(reverse=True)

    if N == 1:
        print(C[0] * 2 % MOD)
        exit()

    first = pow(2, N-1, MOD)
    d = pow(2, N-2, MOD)
    num = [first + d*i for i in range(N)]

    ans = 0
    for c, a in zip(C, num):
        ans += c * a
        ans %= MOD
    print(ans * pow(2, N, MOD) % MOD)


if __name__ == "__main__":
    main()
