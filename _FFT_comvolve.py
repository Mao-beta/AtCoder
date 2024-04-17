import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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

import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7

def fft_convolve(f, g, MOD=MOD):
    """
    数列 (多項式) f, g の畳み込みの計算．上下 15 bitずつ分けて計算することで，
    30 bit以下の整数，長さ 250000 程度の数列での計算が正確に行える．
    """
    fft = np.fft.rfft
    ifft = np.fft.irfft
    Lf = len(f)
    Lg = len(g)
    L = Lf + Lg - 1
    fft_len = 1 << L.bit_length()
    fl = f & (1 << 15) - 1
    fh = f >> 15
    gl = g & (1 << 15) - 1
    gh = g >> 15

    def conv(f, g):
        return ifft(fft(f, fft_len) * fft(g, fft_len))[:L]

    x = conv(fl, gl) % MOD
    y = conv(fl + fh, gl + gh) % MOD
    z = conv(fh, gh) % MOD
    a, b, c = map(lambda x: (x + .5).astype(np.int64), [x, y, z])
    return (a + ((b - a - c) << 15) + (c << 30)) % MOD


def coef_of_generating_function(P, Q, N):
    """compute the coefficient [x^N] P/Q of rational power series.

    Parameters
    ----------
    P : np.ndarray
        numerator.
    Q : np.ndarray
        denominator
        Q[0] == 1 and len(Q) == len(P) + 1 is assumed.
    N : int
        The coefficient to compute.
    """
    def convolve(f, g):
        return fft_convolve(f, g, MOD)

    while N:
        Q1 = Q.copy()
        Q1[1::2] = np.negative(Q1[1::2])
        if N & 1:
            P = convolve(P, Q1)[1::2]
        else:
            P = convolve(P, Q1)[::2]
        Q = convolve(Q, Q1)[::2]
        N >>= 1
    return P[0]


def main():
    # https://yukicoder.me/submissions/479414
    N, P, C = map(int, read().split())

    def dice(nums, n_dice):
        U = nums[-1] * n_dice
        dp = np.zeros((n_dice + 1, U + 1), np.int64)
        dp[0, 0] = 1
        for x in nums:
            for i in range(1, n_dice + 1):
                dp[i, x:] += dp[i - 1, :-x]
        return dp[-1]

    f1 = dice((2, 3, 5, 7, 11, 13), P)
    f2 = dice((4, 6, 8, 9, 10, 12), C)
    f = np.convolve(f1, f2) % MOD

    den = -f
    den[0] += 1
    g = f[::-1].cumsum()[::-1] % MOD
    g[0] = 0

    print(coef_of_generating_function(g, den, N))


if __name__ == "__main__":
    main()
