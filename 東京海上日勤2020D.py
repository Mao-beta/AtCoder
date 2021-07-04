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
    items = [[0,0]] + [NLI() for _ in range(N)]
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    for v, l in querys:
        print(bin(v))




if __name__ == "__main__":
    main()