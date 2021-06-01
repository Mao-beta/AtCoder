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
    A, B, C = NMI()
    g = math.gcd(math.gcd(A, B), C)
    print((A+B+C)//g - 3)


if __name__ == "__main__":
    main()
