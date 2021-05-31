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
    ans = 0
    ans += sum(range(K+1)) * N
    ans += sum(range(N+1)) * K * 100
    print(ans)


if __name__ == "__main__":
    main()
