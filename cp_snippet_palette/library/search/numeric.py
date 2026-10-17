"""k-meansと正規分布CDF。出典: AHC039/main.py, AHC022/main.py。
外部ライブラリ不要。PyPy向け。float演算を使用。Codon未確認。
"""

from math import erf, sqrt
from random import Random


def normal_cdf(x, mean=0.0, sigma=1.0):
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return (1.0 + erf((x - mean) / (sigma * sqrt(2.0)))) / 2.0


def kmeans(points, k, iterations=100, seed=0):
    """Lloyd法。O(iterations*n*k*次元)。ラベルと中心を返す。乱数は局所的。
    空クラスタは中心を保持する。最適解やk個すべてが非空になる保証はない。
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
