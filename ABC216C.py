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
    N = bin(NI())[2:]
    ans = "A"
    for i, b in enumerate(N):
        if i == 0: continue
        if b == "1":
            ans += "BA"
        else:
            ans += "B"
    print(ans)


if __name__ == "__main__":
    main()
