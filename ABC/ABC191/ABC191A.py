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
    V, T, S, D = NMI()
    if V*T <= D <= V*S:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
