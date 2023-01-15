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


def print_err(*args):
    print(*args, file=sys.stderr)


def case_corner(N, A):
    for ans in combinations(range(-20, 20), N-1):
        ans = list(ans)
        ans.sort()
        s = 0
        for x, a in zip(ans, A):
            s += x * a
        ans.append(-s)
        if ans[-1] <= 10**20 and ans[-2] < ans[-1]:
            return ans, True

    return [], False

def main(N, A):
    if A[-1] == -1:
        A = [-a for a in A]

    if N == 1:
        print("Yes")
        print(0)
        return

    if N == 2:
        if A[0] == A[1]:
            print("Yes")
            print(-1, 1)
            return
        else:
            print("No")
            return

    # if sum(A) == 0:
    #     print("No")
    #     return


    ans = list(range(N-1))
    L = 0
    for x, a in zip(ans, A):
        L += x * a
    ans.append(-L)

    # 左を全部1下げると差がg縮まる
    g = sum(A[:-1]) + 1
    gap = ans[-1] - ans[-2]
    if gap <= 0:
        gap = abs(gap)
        if g > 0:
            k = (gap + g-1) // g + 1
            for i in range(N-1):
                ans[i] -= k
            gap -= k * g
            ans[-1] = ans[-2] - gap
        elif g < 0:
            g = abs(g)
            k = (gap + g - 1) // g + 1
            for i in range(N - 1):
                ans[i] += k
            gap -= k * g
            ans[-1] = ans[-2] - gap
        else:
            g = sum(A[:-2])
            if g > 0:
                k = (gap + g - 1) // g + 1
                for i in range(N - 2):
                    ans[i] -= k
                gap -= k * g
                ans[-1] = ans[-2] - gap
            else:
                if N <= 6:
                    ans, ok = case_corner(N, A)

                    if not ok:
                        print("No")
                        return

                else:
                    print("No")
                    return

    # print_err(ans)

    for i in range(N-1):
        assert ans[i] < ans[i+1]

    assert ans[0] >= -10**12
    assert ans[-1] <= 10**12

    s = 0
    for x, a in zip(ans, A):
        s += x * a
    assert s == 0

    print("Yes")
    print(*ans)


if __name__ == "__main__":
    N = NI()
    A = NLI()
    main(N, A)

    # for A in product([-1, 1], repeat=N):
    #     print(A)
    #     main(N, A)
