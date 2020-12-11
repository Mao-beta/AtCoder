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
    Ds = [NLI() for _ in range(N)]
    D = [x - y for x, y in Ds]
    cnt = 0
    for d in D:
        if d == 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()