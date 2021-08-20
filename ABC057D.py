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


def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


def main():
    N, A, B = NMI()
    V = NLI()
    V.sort(reverse=True)
    print(sum(V[:A])/A)

    a = V[A-1]
    vn = V.count(a)
    vr = V[:A].count(a)

    if len(set(V[:A])) != 1:
        print(cmb(vn, vr))
    else:
        ans = 0
        for k in range(A, min(B, vn)+1):
            ans += cmb(vn, k)
        print(ans)


if __name__ == "__main__":
    main()
