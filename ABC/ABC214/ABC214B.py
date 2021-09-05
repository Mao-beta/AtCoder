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
    S, T = NMI()
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a + b + c <= S and a * b * c <= T:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
