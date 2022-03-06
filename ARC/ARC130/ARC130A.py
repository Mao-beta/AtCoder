import sys
import math
from collections import Counter

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = SI()
    prev = ""
    ans = 0
    now = 1
    for s in S:
        if s == prev:
            now += 1
        else:
            ans += now * (now-1) // 2
            now = 1

        prev = s

    ans += now * (now-1) // 2
    print(ans)


if __name__ == "__main__":
    main()
