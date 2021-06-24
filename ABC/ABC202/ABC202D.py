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
    A, B, K = NMI()
    ans = ""
    k = 0
    for i in range(A+B):
        na = cmb(A-1+B, B)
        if k + na < K:
            ans += "b"
            B -= 1
            k += na
        else:
            ans += "a"
            A -= 1

        if A == 0:
            ans += "b" * B
            break
        if B == 0:
            ans += "a" * A
            break
    print(ans)


if __name__ == "__main__":
    main()
