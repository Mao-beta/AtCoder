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
EI = lambda m: [NLI() for _ in range(m)]


import matplotlib.pyplot as plt

def main():
    import numpy as np
    import matplotlib.pyplot as plt
    from pathlib import Path

    def plot_histogram(S, dstpath=None):
        # 10000回サンプリング
        samples = np.random.normal(0, S, 10000)

        # ヒストグラムの描画
        plt.hist(samples, bins=50, density=False, alpha=0.7, color='blue')

        # グリッドとタイトルの追加
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.xlim([-100, 100])
        plt.title(f'Histogram of Samples from Normal Distribution (SD={S})')

        # 表示
        # plt.show()

        if dstpath:
            plt.savefig(dstpath, bbox_inches="tight")

        plt.close()



    dst_dir = Path("./gauss_vis/")
    dst_dir.mkdir(exist_ok=True, parents=True)

    for s in range(1, 31):
        S = s**2
        plot_histogram(S / math.sqrt(100), dstpath=dst_dir/f"s=within100_sq100_{s}^2_hist.png")
        plot_histogram(S, dstpath=dst_dir/f"s=within100_{s}^2_hist.png")


if __name__ == "__main__":
    main()
