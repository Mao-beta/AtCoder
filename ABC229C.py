import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, W = NMI()
    AB = [NLI() for _ in range(N)]
    AB.sort(reverse=True)

    now = 0
    ans = 0
    for a, b in AB:
        if now + b <= W:
            now += b
            ans += a * b
        else:
            ans += a * (W - now)
            break

    print(ans)


if __name__ == "__main__":
    main()
