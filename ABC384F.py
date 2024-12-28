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


def sum_of_reduced_values_for_all_pairs(A):
    """
    数列Aの全てのペア(i<=j)について、各ペアの和を2べきで割り続けた後の最終的な値を合計する
    O(N*log(maxA))
    """
    # S[b]: 和が2^bで割れる(Ai, Aj)(i<=j)のペアの総和
    S = [0] * 32
    for b in range(32):
        B = 1 << b
        C = Counter()
        D = defaultdict(int)
        for a in A:
            D[a % B] += a
            C[a % B] += 1
        for a in A:
            if (B - a % B) % B == a % B:
                S[b] += D[(B - a % B) % B] - a + (C[(B - a % B) % B] - 1) * a + a * 2 * 2
            else:
                S[b] += D[(B - a % B) % B] + C[(B - a % B) % B] * a
        S[b] >>= 1
    G = [(S[b] - S[b + 1]) >> b for b in range(31)]
    return sum(G)


def main():
    N = NI()
    A = NLI()
    print(sum_of_reduced_values_for_all_pairs(A))


if __name__ == "__main__":
    main()
