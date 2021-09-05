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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, K = NMI()
    C = NLI()
    zipped, unzipped = compress(set(C))
    C = [zipped[c] for c in C]

    M = len(zipped)
    cnts = [0] * M
    kind = 0
    ans = 0
    for i in range(N):
        if i < K:
            cnts[C[i]] += 1
            if i == K-1:
                tmp = [1 if cnt else 0 for cnt in cnts]
                kind = sum(tmp)

        else:
            out_c = C[i-K]
            in_c = C[i]

            cnts[out_c] -= 1
            if cnts[out_c] == 0:
                kind -= 1

            cnts[in_c] += 1
            if cnts[in_c] == 1:
                kind += 1

        ans = max(ans, kind)

    print(ans)


if __name__ == "__main__":
    main()
