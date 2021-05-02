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
    X = NLI()

    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    bits = []
    for x in X:
        b = 0
        for i, p in enumerate(P):
            if x % p == 0:
                b += 1 << i
        bits.append(b)

    pn = len(P)
    ans = 10**20
    for case in range(1<<pn):
        flag = True
        for b in bits:
            if b & case == 0:
                flag = False

        if flag:
            tmp = 1
            for i, p in enumerate(P):
                if (case>>i) & 1:
                    tmp *= p
                if tmp > ans:
                    flag = False
                    break
        if flag:
            ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
