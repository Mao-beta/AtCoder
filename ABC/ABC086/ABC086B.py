import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    A, B = SI().split()
    N = int(A+B)
    S = set([i**2 for i in range(400)])
    print("Yes" if N in S else "No")


if __name__ == "__main__":
    main()
