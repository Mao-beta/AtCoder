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


import numpy as np
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


def main():
    N = NI()
    A = [NI() for _ in range(N+1)]
    B = [NI() for _ in range(N+1)]
    A = np.array(A)
    B = np.array(B)
    C = fft_convolve(A, B, MOD)[:N+1].sum() % MOD
    print(C)


if __name__ == "__main__":
    main()
