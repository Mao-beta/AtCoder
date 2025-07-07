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


def manacher(s):
    """
    文字列Sから奇数長の最長の回文をO(|S|)で検索するアルゴリズム。
    Sの各文字の間にSには絶対に登場しないダミー文字を挟み込むと、偶数長の回文も見つけられる。
    両端と各文字の間に'$'を挿入すると、「各要素の値-1」がそこを中心とした回文の長さとなる。
    """
    n = len(s)
    radius = [0] * n
    i, j = 0, 0
    while i < n:
        while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
            j += 1
        radius[i] = j
        k = 1
        while i - k >= 0 and i + k < n and k + radius[i - k] < j:
            radius[i + k] = radius[i - k]
            k += 1
        i += k
        j -= k
    return radius


def main():
    S = SI()
    T = [S[0]]
    for i in range(1, len(S)):
        T.append("$")
        T.append(S[i])
    # print(T)
    R = manacher(T)
    # print(R)
    kmax = 0
    for k in range(1, len(T)+1):
        if R[-k] == k:
            kmax = max(kmax, k)
    idx = len(T) - (kmax*2-1)
    res = T + T[:idx][::-1]
    ans = [t for t in res if t != "$"]
    print("".join(ans))


if __name__ == "__main__":
    main()
