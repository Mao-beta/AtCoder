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
    S = [SI() for _ in range(3)]
    T = SI()
    ans = ""
    for x in T:
        x = int(x) - 1
        ans += S[x]
    print(ans)


if __name__ == "__main__":
    main()
