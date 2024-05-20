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


class Bitset:
    '''
        N:       bitの長さ
        add():   xビット目を1にする
        sub():   xビット目を0にする
        count(): 1となるビットの数を取得
        self[x]: xビット目を取得
        bit演算子 &, | 対応
    '''
    def __init__(self, N):
        self.bit_size = 63
        self.bits_size = (N + self.bit_size - 1) // self.bit_size
        self.bits = self.bits_size * [0]
        self.N = N

    def add(self, x):
        self.bits[x // self.bit_size] |= 1 << (x % self.bit_size)

    def sub(self, x):
        self.bits[x // self.bit_size] &= ~(1 << (x % self.bit_size))

    def count(self):
        cnt = 0
        for x in self.bits:
            c = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
            c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
            c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
            c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
            c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
            c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
            cnt += c

        return cnt

    def __and__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] & other.bits[i]

        return _bitset

    def __or__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] | other.bits[i]

        return _bitset

    def __xor__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] ^ other.bits[i]

        return _bitset

    def __getitem__(self, x):
        return (self.bits[x // self.bit_size] >> (x % self.bit_size)) & 1


    def __str__(self):
        res = 0
        for i in range(self.N):
            res |= 1 << self[i]
        return str(self.bits)



def _main():
    N, M = NMI()
    A = EI(N)
    ma = 1000

    ans = 0

    B = [Bitset(N) for _ in range(N)]
    for w in range(M):
        dp = [Bitset(N) for _ in range(ma)]
        for h in range(N):
            a = A[h][w]
            dp[a].add(h)

        for h in range(N):
            B[h] ^= dp[A[h][w]]

    for i in range(N):
        ans += B[i].count()
        if B[i][i]:
            ans -= 1

    print(ans // 2)


def main():
    N, M = NMI()
    A = EI(N)
    ma = 1000

    ans = 0

    B = [0] * N
    for w in range(M):
        dp = [0] * ma
        for h in range(N):
            a = A[h][w]
            dp[a] ^= 1 << h

        for h in range(N):
            B[h] ^= dp[A[h][w]]

    for i in range(N):
        ans += B[i].bit_count()
        if (B[i] >> i) & 1:
            ans -= 1

    print(ans // 2)


if __name__ == "__main__":
    main()
