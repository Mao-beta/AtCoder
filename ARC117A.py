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
    A, B = NMI()

    ans = []
    flag = False
    if A < B:
        A, B = B, A
        flag = True

    ans += [a for a in range(1, A+1)]
    SA = sum(ans)
    BL = [-b for b in range(1, B)]
    ans += BL + [-sum(BL) - SA]

    if flag:
        ans = [-a for a in ans]

    print(*ans)





if __name__ == "__main__":
    main()
