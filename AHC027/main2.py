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


def can_move(i, j, i2, j2, N, h, v):
    # この例では、すべての隣接するマスへの移動を許可
    if not (0 <= i2 < N and 0 <= j2 < N):
        return False
    if abs(i - i2) + abs(j - j2) != 1:
        return False
    if (i2-i == 0 and v[i][min(j, j2)]) == 0 or (j2-j == 0 and h[min(i, i2)][j]) == 0:
        return True
    return False



class Board:
    def __init__(self, N, h, v, d):
        self.N = N
        self.h = h
        self.v = v
        self.d = d
        self.DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.DIR = "RDLU"
        self.all_distances = self.precompute_shortest_paths()

    def can_move(self, i, j, i2, j2):
        # この例では、すべての隣接するマスへの移動を許可
        if not (0 <= i2 < self.N and 0 <= j2 < self.N):
            return False
        if abs(i - i2) + abs(j - j2) != 1:
            return False
        if (i2 - i == 0 and self.v[i][min(j, j2)] == 0) or (j2 - j == 0 and self.h[min(i, i2)][j] == 0):
            return True
        return False

    def precompute_shortest_paths(self):
        def bfs_shortest_path(start):
            # BFSを使用して特定の点からの全点への最短距離を計算
            queue = deque([start])
            distances = [[float('inf') for _ in range(self.N)] for _ in range(self.N)]
            distances[start[0]][start[1]] = 0

            while queue:
                i, j = queue.popleft()

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if self.can_move(i, j, ni, nj) and distances[ni][nj] == float('inf'):
                        queue.append((ni, nj))
                        distances[ni][nj] = distances[i][j] + 1

            return distances

        # 全ての点から全ての点への最短距離を計算
        all_distances = [[[[]] for _ in range(self.N)] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                all_distances[i][j] = bfs_shortest_path((i, j))

        return all_distances

    def tsp_with_path(self, priority_points, tsp_start):
        def nearest_neighbor(start):
            unvisited = set(priority_points)
            tour = [start]
            current_point = start
            if start in unvisited:
                unvisited.discard(start)

            while unvisited:
                next_point, min_distance = None, float('inf')
                path_to_next_point = []

                for point in unvisited:
                    distance = self.all_distances[current_point[0]][current_point[1]][point[0]][point[1]]
                    if distance < min_distance:
                        next_point, min_distance = point, distance

                if next_point:
                    path_to_next_point = self.reconstruct_path(current_point, next_point)
                    tour.extend(path_to_next_point[1:])  # Exclude the starting point
                    unvisited.remove(next_point)
                    current_point = next_point

            return tour

        return nearest_neighbor(tsp_start)

    def reconstruct_path(self, start, end):
        path = [end]
        while path[-1] != start:
            current_i, current_j = path[-1]
            neighbors = [(current_i + di, current_j + dj) for di, dj in self.DIJ if
                         self.can_move(current_i, current_j, current_i + di, current_j + dj)]
            next_point = min(neighbors, key=lambda p: self.all_distances[start[0]][start[1]][p[0]][p[1]])
            path.append(next_point)

        return path[::-1]  # パスを反転して返す

    def reconstruct_movement(self, route):
        # ルートから実際の移動（RDLUの文字列）を復元する関数
        movement = ""
        for i in range(len(route) - 1):
            current_i, current_j = route[i]
            next_i, next_j = route[i + 1]

            for k, (di, dj) in enumerate(self.DIJ):
                if current_i + di == next_i and current_j + dj == next_j:
                    movement += self.DIR[k]
                    break

        return movement



def tsp_approximation_return_to_start(N, priority_points, h, v, all_distance):
    def nearest_neighbor_return_to_start(start):
        unvisited = set(priority_points)
        tour = [start]

        current_point = start
        if current_point in unvisited:
            unvisited.remove(current_point)

        while unvisited:
            next_point = None
            min_distance = float('inf')
            path_to_next_point = []

            for point in unvisited:
                distance, path = compute_distance_with_path(current_point, point, N)
                if distance < min_distance:
                    next_point = point
                    min_distance = distance
                    path_to_next_point = path

            if next_point is not None:
                tour.extend(path_to_next_point[1:])  # Exclude the starting point
                unvisited.remove(next_point)
                current_point = next_point

        # Return to start
        _, path_to_start = compute_distance_with_path(current_point, start, N)
        tour.extend(path_to_start[1:])  # Exclude the starting point

        return tour

    def compute_distance_with_path(point1, point2, N):
        from collections import deque

        queue = deque([([point1], 0)])  # (path, distance)
        visited = set([point1])

        while queue:
            path, distance = queue.popleft()
            current_point = path[-1]
            if current_point == point2:
                return distance, path

            i, j = current_point
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_point = (i + di, j + dj)
                if next_point not in visited and can_move(i, j, i + di, j + dj, N, h, v):
                    new_path = path + [next_point]
                    queue.append((new_path, distance + 1))
                    visited.add(next_point)

        return float('inf'), []

    def reconstruct_path(start, end, shortest_paths):
        # startからendまでのパスを逆にたどって復元する関数
        path = [end]

        while path[-1] != start:
            current_i, current_j = path[-1]
            # 盤面内にある隣接するマスを取得
            neighbors = [(current_i + di, current_j + dj) for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                         if can_move(current_i, current_j, current_i + di, current_j + dj, N, h, v)]
            # 隣接するマスの中で、最短距離が一つ前のマスに該当するマスを選択
            next_point = min(neighbors, key=lambda p: shortest_paths[start[0]][start[1]][p[0]][p[1]])
            path.append(next_point)

        return path[::-1]  # パスを反転して返す

    # (0, 0)から始めてすべての優先マスを訪れ、(0, 0)に戻るルートを見つける
    return nearest_neighbor_return_to_start((0, 0))






def main():
    N = NI()
    h = [list(map(int, SI())) for _ in range(N - 1)]
    v = [list(map(int, SI())) for _ in range(N)]
    d = [list(map(int, input().split())) for _ in range(N)]

    def get_priority_points(cutoff):
        priority_points = []
        for i in range(N):
            for j in range(N):
                if d[i][j] > cutoff:
                    priority_points.append((i, j))
        return priority_points

    routes = []

    all_points = get_priority_points(-1)
    priority_points_50 = get_priority_points(50)
    priority_points_30 = get_priority_points(30)
    priority_points_10 = get_priority_points(10)
    priority_points_5 = get_priority_points(5)

    board = Board(N, h, v, d)
    route = board.tsp_with_path(priority_points_50, (0, 0))
    routes.append(route)
    movement = board.reconstruct_movement(routes[-1])
    print(movement, end="")

    route2 = board.tsp_with_path(priority_points_30, routes[-1][-1])
    routes.append(route2)
    movement2 = board.reconstruct_movement(routes[-1])
    print(movement2, end="")

    route = board.tsp_with_path(priority_points_50, routes[-1][-1])
    routes.append(route)
    movement = board.reconstruct_movement(routes[-1])
    print(movement, end="")

    route3 = board.tsp_with_path(priority_points_10, routes[-1][-1])
    routes.append(route3)
    movement3 = board.reconstruct_movement(routes[-1])
    print(movement3, end="")

    route = board.tsp_with_path(priority_points_50, routes[-1][-1])
    routes.append(route)
    movement = board.reconstruct_movement(routes[-1])
    print(movement, end="")

    route3 = board.tsp_with_path(priority_points_5, routes[-1][-1])
    routes.append(route3)
    movement3 = board.reconstruct_movement(routes[-1])
    print(movement3, end="")

    route = board.tsp_with_path(priority_points_50, routes[-1][-1])
    routes.append(route)
    movement = board.reconstruct_movement(routes[-1])
    print(movement, end="")

    else_points = set(all_points)
    for route in routes:
        else_points -= set(route)

    route4 = board.tsp_with_path(else_points | set(priority_points_50), routes[-1][-1])
    routes.append(route4)
    movement4 = board.reconstruct_movement(routes[-1])
    print(movement4, end="")

    route5 = board.tsp_with_path([(0, 0)], routes[-1][-1])
    routes.append(route5)
    movement5 = board.reconstruct_movement(routes[-1])
    print(movement5)


if __name__ == "__main__":
    main()
