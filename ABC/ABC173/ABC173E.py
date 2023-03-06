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


def main():
    N, K = NMI()
    A = NLI()
    A.sort(key=lambda x: -abs(x))

    if max(A) <= 0 and K % 2:
        ans = 1
        for i in range(K):
            a = A[N-1-i]
            ans *= a
            ans %= MOD
        print(ans)
        exit()

    minus = 0
    ans = 1
    pre_plus = None
    pre_minus = None
    for i in range(K):
        a = A[i]
        ans = ans * abs(a) % MOD
        if a < 0:
            pre_minus = abs(a)
            minus ^= 1
        else:
            pre_plus = a

    if N == K:
        if minus:
            ans = ans * (-1) % MOD
        print(ans)

    elif minus:
        post_plus = None
        post_minus = None
        for i in range(K, N):
            a = A[i]
            if post_plus is None and a >= 0:
                post_plus = a
            if post_minus is None and a < 0:
                post_minus = abs(a)

        if post_plus is not None and pre_plus is not None and post_minus is not None:
            if post_plus * pre_plus > pre_minus * post_minus:
                ans = ans * pow(pre_minus, MOD-2, MOD) * post_plus % MOD
            else:
                ans = ans * pow(pre_plus, MOD-2, MOD) * post_minus % MOD

        elif post_plus is not None:
            ans = ans * pow(pre_minus, MOD - 2, MOD) * post_plus % MOD

        elif pre_plus is not None and post_minus is not None:
            ans = ans * pow(pre_plus, MOD - 2, MOD) * post_minus % MOD

        print(ans)

    else:
        print(ans)


if __name__ == "__main__":
    main()