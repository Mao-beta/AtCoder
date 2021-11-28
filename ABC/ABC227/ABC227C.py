import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    K = 10**4
    ans = 0
    for a in range(1, K):
        for b in range(a, int(10**5.5)+10):
            cmax = N // (a*b)
            if cmax < b:
                break
            else:
                ans += cmax - b + 1

    print(ans)


if __name__ == "__main__":
    main()
