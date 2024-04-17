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

import random
import math


def rand(L, U):
    return random.randint(L, U)


def generate_input(W):
    D = rand(5, 50)
    N = rand(5, 50)
    e = rand(500, 5000) / 10000
    E = round(W ** 2 * e ** 2)

    A = []
    for d in range(D):
        T_d = rand(W ** 2 - math.floor(3 * E / 2), W ** 2 - math.floor(E / 2))
        S = {0, T_d}
        while len(S) < N + 1:
            S.add(rand(1, T_d - 1))

        s = sorted(list(S))
        a_d = [s[k + 1] - s[k] for k in range(N)]
        a_d.sort()
        A.append(a_d)

    return D, N, A


import matplotlib.pyplot as plt


def plot_input(D, N, A):
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = plt.cm.get_cmap('tab20', D)

    for d in range(D):
        x = list(range(N-3))
        y = A[d][:-3]
        ax.plot(x, y, color=colors(d), label=f'Day {d}')

    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Input Data')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()
    plt.close()


def analyze_max(D, N, A):
    M = []
    for d in range(D):
        M.append(max(A[d]))
    return max(M) / 10 ** 6, M

def main():
    W = 1000

    R = []
    Ns = []
    for _ in range(5):
        D, N, A = generate_input(W)
        # print(D, N)
        # print(*A, sep="\n")
        plot_input(D, N, A)
        Mratio, M = analyze_max(D, N, A)
        R.append(Mratio)
        Ns.append(N)

    # plt.scatter(Ns, R)
    # plt.show()
    # plt.close()


if __name__ == "__main__":
    main()
