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
    for i in range(1, 10**6):
        s = str(i)
        x = int(s*2)
        if x <= N:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
