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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def compress(S):
    """ 座標圧縮 """

    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


# 配列から累積和を返す
def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
    N, C = NMI()
    S = [NLI() for _ in range(N)]
    S = [[a-1, b, c] for a, b, c in S]
    day_set = set()
    for a, b, _ in S:
        day_set.add(a)
        day_set.add(b)

    zipped, unzipped = compress(list(day_set))

    imos = [0]*(len(zipped))

    for a, b, c in S:
        a_idx = zipped[a]
        b_idx = zipped[b]
        imos[a_idx] += c
        imos[b_idx] -= c

    cum = make_cumulative(imos)
    price = [min(cu, C) for cu in cum]

    ans = 0
    for i, p in enumerate(price[1:]):
        if p == 0: continue
        ans += (unzipped[i+1] - unzipped[i]) * p
    print(ans)



if __name__ == "__main__":
    main()
