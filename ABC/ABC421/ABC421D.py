import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def main():
    Ht, Wt, Ha, Wa = NMI()
    N, M, L = NMI()
    SA = deque([SLI() for _ in range(M)])
    TB = deque([SLI() for _ in range(L)])
    D = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    H = Ha - Ht
    W = Wa - Wt
    D2 = dict()
    for s, t in product("UDLR", "UDLR"):
        hs, ws = D[s]
        ht, wt = D[t]
        D2[s+t] = (ht-hs, wt-ws)
    # print(D2)
    ans = 0
    while SA and TB:
        s, a = SA.popleft()
        t, b = TB.popleft()
        a, b = int(a), int(b)
        h, w = D2[s+t]
        if a <= b:
            x = a
            if h == w == 0 and H == W == 0:
                ans += x
            elif h == w == 0:
                pass
            # 以下は原点にいない
            elif h == 0: # 横移動のみ
                if H != 0:
                    pass
                elif W % 2:
                    pass
                else: # 原点から横に偶数マス
                    if W > 0 and w < 0 and W+x*w <= 0:
                        ans += 1
                    elif W < 0 and w > 0 and W+x*w >= 0:
                        ans += 1
                    else:
                        pass
            elif w == 0: # 縦移動のみ
                if W != 0:
                    pass
                elif H % 2:
                    pass
                else: # 原点から縦に偶数マス
                    if H > 0 and h < 0 and H+x*h <= 0:
                        ans += 1
                    elif H < 0 and h > 0 and H+x*h >= 0:
                        ans += 1
                    else:
                        pass
            elif H == W:
                if H < 0 and h == 1 and w == 1 and H + x*h >= 0:
                    ans += 1
                elif H > 0 and h == -1 and w == -1 and H + x*h <= 0:
                    ans += 1
            elif H == -W:
                if H < 0 and h == 1 and w == -1 and H + x*h >= 0:
                    ans += 1
                elif H > 0 and h == -1 and w == 1 and H + x*h <= 0:
                    ans += 1

            H += x*h
            W += x*w
            b -= a
            if b > 0:
                TB.appendleft([t, str(b)])

        else:
            x = b
            if h == w == 0 and H == W == 0:
                ans += x
            elif h == w == 0:
                pass
            # 以下は原点にいない
            elif h == 0:  # 横移動のみ
                if H != 0:
                    pass
                elif W % 2:
                    pass
                else:  # 原点から横に偶数マス
                    if W > 0 and w < 0 and W + x * w <= 0:
                        ans += 1
                    elif W < 0 and w > 0 and W + x * w >= 0:
                        ans += 1
                    else:
                        pass
            elif w == 0:  # 縦移動のみ
                if W != 0:
                    pass
                elif H % 2:
                    pass
                else:  # 原点から縦に偶数マス
                    if H > 0 and h < 0 and H + x * h <= 0:
                        ans += 1
                    elif H < 0 and h > 0 and H + x * h >= 0:
                        ans += 1
                    else:
                        pass
            elif H == W:
                if H < 0 and h == 1 and w == 1 and H + x*h >= 0:
                    ans += 1
                elif H > 0 and h == -1 and w == -1 and H + x*h <= 0:
                    ans += 1
            elif H == -W:
                if H < 0 and h == 1 and w == -1 and H + x*h >= 0:
                    ans += 1
                elif H > 0 and h == -1 and w == 1 and H + x*h <= 0:
                    ans += 1

            H += x * h
            W += x * w
            a -= b
            if a > 0:
                SA.appendleft([s, str(a)])
    print(ans)


if __name__ == "__main__":
    main()
