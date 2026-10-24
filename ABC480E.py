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

# ライブラリ https://github.com/Mao-beta/AtCoder


def main():
    N = NI()
    # maxで長さ19
    ans = 0
    for a in range(1, 10**6+1):
        for n in range(3, 20):
            t = a
            for i in range(n-1):
                t *= a
                if t > N:
                    break
            if t > N:
                break

            def judge(X):
                now = a
                v = a
                for i in range(n-1):
                    v += X
                    now *= v
                    if now > N:
                        return False
                return True

            ok = 0
            ng = 10**9
            while abs(ok - ng) > 1:
                X = (ok + ng) // 2
                if judge(X):
                    ok = X
                else:
                    ng = X

            # print(ok)
            ans += ok
    print(ans)


if __name__ == "__main__":
    main()
