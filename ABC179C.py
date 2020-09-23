import sys
import math
from collections import defaultdict
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
    ans = 0
    for a in range(1, N):
        ans += N // a
        if N % a == 0:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()