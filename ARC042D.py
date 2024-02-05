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
    X, P, A, B = NMI()
    cutoff = 1<<24
    if B-A <= cutoff:
        now = pow(X, A-1, P)
        ans = P-1
        for i in range(A, B+1):
            now = now * X % P
            ans = min(ans, now)
        print(ans)

    else:
        xa_inv = pow(X, -A, P)
        for r in range(cutoff+1):
            t = r * xa_inv % P
            k = mod_log(X, t, P)
            if k < 0 or k > B-A:
                continue
            print(r)
            return


if __name__ == "__main__":
    main()
