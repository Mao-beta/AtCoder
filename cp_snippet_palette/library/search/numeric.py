"""k-meansと正規分布CDF。出典: AHC039/main.py, AHC022/main.py。

外部ライブラリ不要。PyPy向け。float演算を使用。Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    normal_cdf(0)  # => 0.5
    labels, centers = kmeans([(0, 0), (2, 2)], k=1)
    labels, centers  # => ([0, 0], [[1.0, 1.0]])
"""

from math import erf, sqrt
from random import Random


def normal_cdf(x, mean=0.0, sigma=1.0):
    """平均mean、標準偏差sigma>0の正規分布でP(X<=x)をfloatで返す。
    sigmaは分散ではなく標準偏差。既定は標準正規分布。O(1)。
    x/mean/sigmaは実数。追加空間O(1)。
    """
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return (1.0 + erf((x - mean) / (sigma * sqrt(2.0)))) / 2.0


def kmeans(points, k, iterations=100, seed=0):
    """同じ次元の数値ベクトル列pointsをk群に分け、(labels,centers)を返す。
    labels[i]は0..k-1の群番号、centers[j]はfloatの中心座標list。
    1<=k<=len(points)、iterations>0。seed固定で初期中心を再現する。
    O(iterations*n*k*次元)。空クラスタは中心を保持し、最適性・全群非空は保証しない。
    pointsは長さDで揃った数値ベクトルの列。n=len(points)、kは群数、iterationsは最大反復数の正整数、seedは初期中心を再現する整数。
    追加空間O(n+kD)。
    """
    n = len(points)
    if not 1 <= k <= n or iterations <= 0:
        raise ValueError("1<=k<=n and positive iterations required")
    dimension = len(points[0])
    if dimension == 0 or any(len(p) != dimension for p in points):
        raise ValueError("inconsistent dimensions")
    centers = [[float(x) for x in points[i]] for i in Random(seed).sample(range(n), k)]
    labels = [-1] * n
    for _ in range(iterations):
        new_labels = [
            min(
                range(k),
                key=lambda j: sum(
                    (p[d] - centers[j][d]) ** 2 for d in range(dimension)
                ),
            )
            for p in points
        ]
        if new_labels == labels:
            break
        labels = new_labels
        sums = [[0.0] * dimension for _ in range(k)]
        counts = [0] * k
        for p, j in zip(points, labels):
            counts[j] += 1
            for d in range(dimension):
                sums[j][d] += p[d]
        for j in range(k):
            if counts[j]:
                centers[j] = [x / counts[j] for x in sums[j]]
    return labels, centers
