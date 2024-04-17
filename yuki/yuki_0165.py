import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, B = NMI()
    XYP = EI(N)
    X = sorted(list(set(x for x, _, _ in XYP)))
    Y = sorted(list(set(y for _, y, _ in XYP)))
    ZX, _ = compress(X)
    ZY, _ = compress(Y)
    XYP = [[ZX[x], ZY[y], p] for x, y, p in XYP]
    ans = 0
    for i in range(len(X)):
        for j in range(i+1, len(X)+1):
            P = [0] * len(ZY)
            X = [0] * len(ZY)
            for x, y, p in XYP:
                if i <= x < j:
                    P[y] += p
                    X[y] += 1
            # 尺取り
            D = deque()
            tmp = 0
            r = 0
            s = 0
            x = 0
            for l in range(len(ZY)):
                if r < l:
                    r = l
                while r < len(ZY) and s + P[r] <= B:
                    D.append(P[r])
                    s += P[r]
                    x += X[r]
                    r += 1
                tmp = max(tmp, x)
                if D:
                    p = D.popleft()
                    s -= p
                    x -= X[l]

            ans = max(ans, tmp)


    print(ans)


if __name__ == "__main__":
    main()
