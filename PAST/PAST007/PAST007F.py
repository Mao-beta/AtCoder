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
    DST = [NLI() for _ in range(N)]
    table = [[0]*25 for _ in range(10**5+1)]

    for d, s, t in DST:
        for x in range(s, t):
            if table[d][x]:
                print("Yes")
                exit()
            else:
                table[d][x] = 1

    print("No")


if __name__ == "__main__":
    main()
