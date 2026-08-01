import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product, repeat

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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


# 行列積（任意サイズ）
def mul_matrix(A, B, mod=998244353):
    Ah = len(A)
    Aw = len(A[0])
    Bh = len(B)
    Bw = len(B[0])
    assert Aw == Bh
    C = [[0] * Bw for _ in range(Ah)]
    for h in range(Ah):
        Arow = A[h]
        Crow = C[h]
        for i in range(Aw):
            a = Arow[i]
            Brow = B[i]
            for w in range(Bw):
                Crow[w] = (Crow[w] + a * Brow[w]) % mod
    return C

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=998244353):
    assert len(A) == len(A[0])
    bitn = len(bin(n)) - 2
    pows = []
    size = len(A)
    E = [[0] * size for _ in range(size)]
    for i in range(size):
        E[i][i] = 1

    pows.append(A)
    ans = E

    for i in range(bitn):
        if (n >> i) & 1:
            ans = mul_matrix(pows[-1], ans, mod)
        pows.append(mul_matrix(pows[-1], pows[-1], mod))

    return ans


def main(N, K, S):
    S = list(S)
    banned = set()
    for i in range(len(S)):
        for j in range(len(S)):
            if i == j:
                continue
            if S[i] in S[j]:
                banned.add(j)
    S = [S[i] for i in range(len(S)) if i not in banned]
    S = set(S)
    SS = set()
    SS.add("")
    for s in S:
        for i in range(1, len(s)+1):
            SS.add(s[:i])
    Z, UZ = compress(SS)
    # print(Z)
    ZN = len(Z)
    A = [[0]*ZN for _ in range(ZN)]
    for T, t in Z.items():
        for x in range(26):
            TX = T + chr(ord('a') + x)
            for l in range(len(TX)+1):
                TXl = TX[l:]
                if TXl in Z:
                    if TXl not in S:
                        A[t][Z[TXl]] += 1
                    break
    # print(*A, sep="\n")
    B = pow_matrix(A, N, MOD99)
    # print(*B, sep="\n")

    return sum(B[0]) % MOD99


def guchoku(N, K, S):
    ans = 0
    for P in product("abcdefghijklmnopqrstuvwxyz", repeat=N):
        P = "".join(P)
        ok = True
        for SS in S:
            if SS in P:
                ok = False
                break
        ans += int(ok)
    return ans


if __name__ == "__main__":
    N, K = NMI()
    S = set(SI() for _ in range(K))
    ans = main(N, K, S)
    print(ans)
    exit()
    for _ in range(1000):
        N = 3
        from random import randint
        K = 10
        S = set()
        for _ in range(K):
            SS = [chr(ord("a")+randint(0, 25)) for _ in range(randint(1, N))]
            SS = "".join(SS)
            S.add(SS)
        ans = main(N, K, S)
        gu = guchoku(N, K, S)
        print((N, K, S, ans, gu))
        assert ans == gu, (N, K, S, ans, gu)
