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
    T = NI()
    for _ in range(T):
        N = NI()
        H = NLI()
        G = 0
        for h in H:
            g = 0
            for i in range(2, 10**3 + 1):
                while h % i == 0:
                    h //= i
                    g += 1
            if h != 1:
                g += 1
            G ^= g
        print(1 if G else 2)


if __name__ == "__main__":
    main()
