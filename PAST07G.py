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
    N = NI()
    ans = []
    now = 1
    while N != 0:
        rem = N % 3
        if rem == 0:
            pass
        elif rem == 1:
            ans.append(now)
            N -= 1
        else:
            ans.append(-now)
            N += 2

        N //= 3
        now *= 3

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
