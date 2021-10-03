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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]
    S = []
    for a, b in AB:
        S.append((a, 0))
        S.append((a+b, 1))
    S.sort()
    ans = [0] * N
    num = 0
    prev = S[0][0]
    for x, b in S:
        if num > 0:
            ans[num-1] += x - prev
        if b == 0:
            num += 1
        else:
            num -= 1
        prev = x

    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
