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
    A, B, C = NMI()
    D = {A: "A", B: "B", C:"C"}
    x = sorted([A, B, C])[1]
    print(D[x])


if __name__ == "__main__":
    main()
