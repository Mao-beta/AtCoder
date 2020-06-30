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
    S = SI()
    l = len(S)
    ans = 0
    for case in range(2**(l-1)):
        j = 0
        N = int(S)
        ans += N % 10
        for i in range(l-1):
            if (case >> i) & 1:
                j = 0
            else:
                j += 1
            ans += int(S[-(i+2)]) * 10**j

    print(ans)


if __name__ == "__main__":
    main()