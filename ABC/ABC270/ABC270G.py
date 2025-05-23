import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


# X^K ≡ Y (mod M) となるような K を求める O(√M)
def mod_log(X, Y, M):
    # https://drken1215.hatenablog.com/entry/2020/11/04/045400

    # X^0 - X^√M までの余りと、それが何回目かを全探索して辞書で持つ
    # Yの方から√M回ぶん（Giant-step）ずつ戻ると、上記に存在する余りになる（ならなければそもそも存在しない）
    # Xの累乗をMで割った余りの周期はM以下なのでGiant-stepで目的の値を飛び越すことはない

    X %= M
    Y %= M

    lo = -1
    hi = M
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid * mid >= M:
            hi = mid
        else:
            lo = mid

    sqrtM = hi

    apow = dict()
    amari = X
    for r in range(1, sqrtM+1):
        if amari not in apow:
            apow[amari] = r
        amari = amari * X % M

    A = pow(pow(X, M-2, M), sqrtM, M)
    amari = Y
    for q in range(sqrtM):
        if amari == 1 and q > 0:
            return q * sqrtM
        elif amari in apow:
            return q * sqrtM + apow[amari]
        amari = amari * A % M

    return -1


def main():
    T = NI()
    for _ in range(T):
        P, A, B, S, G = NMI()

        if S == G:
            print(0)
            continue

        if A == 1:
            if B != 0:
                print((G-S) * pow(B, P-2, P) % P)
                continue
            else:
                print(-1)
                continue

        if A == 0:
            if G == B:
                print(1)
                continue
            else:
                print(-1)
                continue

        bunsi = (G * (A-1) + B) % P
        bunbo = ((A-1) * S + B) % P

        if bunbo == 0:
            print(-1)
            continue

        if bunsi == 0:
            print(-1)
            continue

        X = bunsi * pow(bunbo, P-2, P) % P

        i = mod_log(A, X, P)
        print(i)


if __name__ == "__main__":
    main()
