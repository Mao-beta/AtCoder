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
    N, K = NMI()
    ans = N
    for k in range(K):
        if ans % 200 == 0:
            ans = ans // 200
        else:
            ans = ans * 1000 + 200
    print(ans)


if __name__ == "__main__":
    main()
