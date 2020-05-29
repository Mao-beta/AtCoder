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


#隣接リスト 1-order
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    A, B, m = NMI()
    g = math.gcd(A, B)
    one_sum = A // g
    vec = [1, 1]
    square = sq_pow([[10**g, 1], [0, 1]], one_sum-1, m)

    ans = square[0][0] * vec[0] + square[0][1] * vec[1]
    ans %= m
    ans *= keta_to_one(B) % m
    print(ans%m)


def sq_mul(a, b, m): # a, bは同じ形の正方行列
    H = len(a)
    res = make_grid(H, H, 0)
    for h in range(H):
        for w in range(H):
            for i in range(H):
                res[h][w] += a[h][i] * b[i][w] % m
    return res


def sq_pow(a, exp, m):
    res = make_grid(len(a), len(a), 0)
    for i in range(len(a)):
        res[i][i] = 1
    if exp == 0: return res
    else:
        while exp >= 1:
            if exp == 1:
                return res
            elif exp % 2:
                res = sq_mul(res, a, m)
                exp -= 1
            else:
                res = sq_mul(res, res, m)
                exp = exp // 2


def pow_mod(base, exp, m):
    if exp == 1:
        return base % m
    elif exp % 2:
        return pow_mod(base, exp-1, m) * base % m
    else:
        return pow_mod(base, exp//2, m) ** 2 % m


def one_zero_mod(one_sum, zero_gap, m):
    res = 0
    jump = zero_gap + 1
    num = one_sum
    for i in range(num):
        res *= pow_mod(10, jump, m)
        res += 1
    return res % m


def keta_to_one(keta):
    res = 0
    for i in range(keta):
        res += 10**i
    return res

if __name__ == "__main__":
    main()