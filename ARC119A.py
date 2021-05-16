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


def main():
    N = NI()
    ans = 10**50
    for b in range(61):
        B = pow(2, b)
        a = N // B
        c = N % B
        ans = min(ans, a+b+c)
    print(ans)


if __name__ == "__main__":
    main()
