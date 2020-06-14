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
    N = NI()
    A = NLI()
    nowRGB = [0, 0, 0]
    ans = 1
    for a in A:
        ans *= nowRGB.count(a) % MOD
        for i in range(3):
            if nowRGB[i] == a:
                nowRGB[i] += 1
                break

    print(ans%MOD)



if __name__ == "__main__":
    main()