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

import random
import math


def kmeans(points, K, max_iterations=100):
    # 初期クラスタの中心をランダムに選択
    centers = random.sample(points, K)

    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    for _ in range(max_iterations):
        # 各点のクラスタ番号を記録するリスト
        clusters = [[] for _ in range(K)]

        # 各点を最近のクラスタに割り当て
        for point in points:
            distances = [euclidean_distance(point, center) for center in centers]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        # クラスタの中心を再計算
        new_centers = []
        for cluster in clusters:
            if cluster:
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                new_centers.append((avg_x, avg_y))
            else:
                # クラスタが空の場合はランダムな点を新しい中心にする
                new_centers.append(random.choice(points))

        # 中心が変わらなければ収束とみなして終了
        if new_centers == centers:
            break
        centers = new_centers

    # 各点のクラスタ番号を計算
    result = []
    for point in points:
        distances = [euclidean_distance(point, center) for center in centers]
        cluster_index = distances.index(min(distances))
        result.append(cluster_index)

    return result


# import matplotlib.pyplot as plt
import random


def plot_kmeans(points, result, centers):
    # 各クラスタの色をランダムに設定
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(centers))]

    # 各クラスタの点をプロット
    for cluster_index in range(len(centers)):
        cluster_points = [points[i] for i in range(len(points)) if result[i] == cluster_index]
        if cluster_points:  # クラスタに点が含まれる場合のみプロット
            x, y = zip(*cluster_points)
            plt.scatter(x, y, color=colors[cluster_index], s=1, label=f"Cluster {cluster_index}")

    # クラスタ中心をプロット
    center_x, center_y = zip(*centers)
    plt.scatter(center_x, center_y, color='black', marker='x', s=100, label="Centers")

    # グラフの装飾
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("K-means Clustering")
    # plt.legend()
    plt.show()


# K-meansクラスタリングの関数（前述の関数に変更を加え、クラスタ中心も返すようにしたもの）
def kmeans(points, K, max_iterations=100):
    centers = random.sample(points, K)

    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    for _ in range(max_iterations):
        clusters = [[] for _ in range(K)]

        for point in points:
            distances = [euclidean_distance(point, center) for center in centers]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        new_centers = []
        for cluster in clusters:
            if cluster:
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                new_centers.append((avg_x, avg_y))
            else:
                new_centers.append(random.choice(points))

        if new_centers == centers:
            break
        centers = new_centers

    result = []
    for point in points:
        distances = [euclidean_distance(point, center) for center in centers]
        cluster_index = distances.index(min(distances))
        result.append(cluster_index)

    return result, centers


def plot_kmeans_with_bounding_rectangles(points, result, centers, rectangles):
    # 各クラスタの色をランダムに設定
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(centers))]

    # 各クラスタの点をプロット
    for cluster_index, center in enumerate(centers):
        cluster_points = [points[i] for i in range(len(points)) if result[i] == cluster_index]
        if cluster_points:
            x, y = zip(*cluster_points)
            plt.scatter(x, y, color=colors[cluster_index], s=1, label=f"Cluster {cluster_index}")

    # クラスタ中心をプロット
    center_x, center_y = zip(*centers)
    plt.scatter(center_x, center_y, color='black', marker='x', s=100, label="Centers")

    # 各クラスタの85%以上の点をカバーする長方形をプロット
    for cluster_index, rect in enumerate(rectangles):
        if rect:
            (x_min, y_min), (x_max, y_max) = rect
            plt.plot([x_min, x_max, x_max, x_min, x_min],
                     [y_min, y_min, y_max, y_max, y_min],
                     color=colors[cluster_index], linestyle="--", linewidth=2,
                     label=f"Cluster {cluster_index} Bounding Box")

    # グラフの装飾
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("K-means Clustering with Bounding Rectangles")
    # plt.legend()
    plt.show()


# 前述のmin_bounding_rectangle_85関数
def min_bounding_rectangle_95(points, result, centers, coverage=0.95):
    rectangles = []

    for cluster_index, center in enumerate(centers):
        # クラスタに属する点を取得
        cluster_points = [points[i] for i in range(len(points)) if result[i] == cluster_index]

        if not cluster_points:
            rectangles.append(None)
            continue

        # クラスタの点数
        N = len(cluster_points)

        # X座標とY座標を抽出してソート
        x_coords = sorted(p[0] for p in cluster_points)
        y_coords = sorted(p[1] for p in cluster_points)

        # 下位2.5%と上位2.5%を除いたインデックス
        lower_index = int(N * 0.025)
        upper_index = int(N * 0.975) - 1  # インデックスは0から始まるので、1を引く

        # 85%以上の点をカバーする範囲を取得
        x_min = x_coords[lower_index]
        x_max = x_coords[upper_index]
        y_min = y_coords[lower_index]
        y_max = y_coords[upper_index]

        # 長方形の左下と右上の座標を保存
        rectangles.append(((x_min, y_min), (x_max, y_max)))

    return rectangles


from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n
        self.members = defaultdict(set)

        for i in range(n):
            self.members[i].add(i)

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)

        self.members[x] |= self.members[y]
        self.members[y] = set()

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_members(self, x):
        root = self.find(x)
        return self.members[root]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)

    def all_group_members(self):
        return self.members

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


def are_overlapping(rect1, rect2):
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2
    return not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)


def visualize_rectangles(rectangles):
    fig, ax = plt.subplots()

    for rect in rectangles:
        (x_min, y_min), (x_max, y_max) = rect
        width = x_max - x_min
        height = y_max - y_min

        # ランダムな色を生成
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        # 長方形を描画
        ax.add_patch(plt.Rectangle((x_min, y_min), width, height, edgecolor="black", facecolor=color, alpha=0.5))

    # 軸ラベルとタイトルの設定
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    ax.set_title("Visualization of Rectangles")
    ax.set_aspect("equal", adjustable="box")

    # 可視化範囲を調整
    all_x = [x_min for (x_min, _), _ in rectangles] + [x_max for _, (x_max, _) in rectangles]
    all_y = [y_min for (_, y_min), _ in rectangles] + [y_max for _, (_, y_max) in rectangles]
    ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
    ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

    plt.show()


def main():
    N = NI()
    saba = EI(N)
    iwashi = EI(N)

    MX = 10**5
    MY = 10**5
    # points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(100)]
    K = 10

    # K-meansクラスタリングの実行
    result, centers = kmeans(saba, K)

    # 結果の可視化
    # plot_kmeans(saba, result, centers)

    # クラスタリング結果を使って長方形を計算
    rectangles = min_bounding_rectangle_95(saba, result, centers)
    # plot_kmeans_with_bounding_rectangles(saba, result, centers, rectangles)

    RN = len(rectangles)
    uf = UnionFind(RN)
    Dists = []
    for i in range(RN):
        cxi, cyi = centers[i]
        for j in range(i+1, RN):
            cxj, cyj = centers[j]
            m = abs(cxi-cxj) + abs(cyi-cyj)
            Dists.append([m, i, j])
    Dists.sort()
    for dist, i, j in Dists:
        if uf.is_same(i, j):
            continue

        if are_overlapping(rectangles[i], rectangles[j]):
            uf.unite(i, j)
            continue

        (xi, yi), (Xi, Yi) = rectangles[i]
        (xj, yj), (Xj, Yj) = rectangles[j]
        x = max(xi, xj)
        X = min(Xi, Xj)
        y = max(yi, yj)
        Y = min(Yi, Yj)
        if x <= X:
            nrect = ((x, min(Yi, Yj)), (X, max(yi, yj)))
            rectangles.append(nrect)
            uf.unite(i, j)
        elif y <= Y:
            nrect = ((min(Xi, Xj), y), (max(xi, xj), Y))
            rectangles.append(nrect)
            uf.unite(i, j)

    # print(uf.group_num)
    # visualize_rectangles(rectangles)

    def compress_coordinates(_rectangles):
        rectangles = _rectangles[:] + [((-MX-1, -MY-1), (MX+1, MY+1))]
        x_coords = sorted(set(x for rect in rectangles for x in (rect[0][0], rect[1][0])))
        y_coords = sorted(set(y for rect in rectangles for y in (rect[0][1], rect[1][1])))

        x_compressed = {x: i for i, x in enumerate(x_coords)}
        y_compressed = {y: i for i, y in enumerate(y_coords)}

        return x_compressed, y_compressed, x_coords, y_coords

    def create_grid(rectangles, x_compressed, y_compressed):
        grid = [[0] * (len(y_compressed)) for _ in range(len(x_compressed))]
        for (x_min, y_min), (x_max, y_max) in rectangles:
            for x in range(x_compressed[x_min], x_compressed[x_max]):
                for y in range(y_compressed[y_min], y_compressed[y_max]):
                    grid[x][y] = 1
        return grid

    def find_outer_boundary(grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右, 下, 左, 上
        boundary = []

        # 開始位置の探索
        start = None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        if not start:
            return []

        # 右手法で外周を探索
        x, y = start
        dir_idx = 0  # 初期方向は「右」
        boundary.append((x, y))
        initial_direction = dir_idx  # 開始方向を記録
        initial_position = (x, y)  # 開始位置を記録

        checks = [[(0, 0), (-1, 0)],
                  [(0, 0), (0, -1)],
                  [(-1, -1), (0, -1)],
                  [(-1, -1), (-1, 0)]]

        while True:
            # 進行方向の周囲が2マス1ならすすむ
            # print(x, y)
            nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]
            if nx == initial_position[0] and ny == initial_position[1]:
                break

            if grid[nx-1][ny-1] + grid[nx-1][ny] + grid[nx][ny-1] + grid[nx][ny] == 2:
                x, y = nx, ny
                continue

            boundary.append((nx, ny))
            x, y = nx, ny
            # 次の方向の決定
            for nd, (dx, dy) in enumerate(directions):
                if dir_idx == nd or dir_idx == (nd+2) % 4:
                    continue
                (cx1, cy1), (cx2, cy2) = checks[nd]
                if grid[x+cx1][y+cy1] == grid[x+cx2][y+cy2]:
                    continue
                dir_idx = nd
                break
            # print(x, y, dir_idx)

        return boundary

    def decompress_boundary(boundary, x_coords, y_coords):
        decompressed_boundary = []
        for x, y in boundary:
            decompressed_boundary.append((x_coords[x], y_coords[y]))
        return decompressed_boundary

    def get_outer_boundary(rectangles):
        # ステップ 1: 座標を圧縮
        x_compressed, y_compressed, x_coords, y_coords = compress_coordinates(rectangles)

        # ステップ 2: 圧縮座標に基づいてグリッドを作成
        grid = create_grid(rectangles, x_compressed, y_compressed)

        # print(*grid, sep="\n")

        # ステップ 3: 外周の探索
        boundary = find_outer_boundary(grid)

        # ステップ 4: 圧縮座標を元の座標に戻す
        decompressed_boundary = decompress_boundary(boundary, x_coords, y_coords)

        return decompressed_boundary

    outer_boundary = get_outer_boundary(rectangles)
    # print("Outer boundary vertices:", outer_boundary)
    L = 0
    for i, (x, y) in enumerate(outer_boundary):
        nx, ny = outer_boundary[(i+1)%len(outer_boundary)]
        L += abs(nx-x) + abs(ny-y)
    if L > 400000:
        print(4)
        (xi, yi), (Xi, Yi) = rectangles[0]
        print(xi, yi)
        print(xi, Yi)
        print(Xi, Yi)
        print(Xi, yi)
        return

    print(len(outer_boundary))
    for x, y in outer_boundary:
        print(x, y)


if __name__ == "__main__":
    main()
