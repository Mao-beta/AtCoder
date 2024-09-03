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


def main():
    N = NI()
    UVL = EI(N-1)
    UVL = [[x-1, y-1, w] for x, y, w in UVL]
    G = [[] for _ in range(N)]
    for u, v, l in UVL:
        G[u].append([v, l])
        G[v].append([u, l])

    scores = []
    seen = set()

    def bfs(s):
        # bfsする
        # 最長パス上でまだ分岐がある点をrootsにappend

        # 初期化
        max_dist = defaultdict(lambda: 0)
        max_dist[s] = 0
        parent = {s: None}

        # BFSキュー
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v, weight in G[u]:
                if v in seen:
                    continue
                if v == parent[u]:
                    continue
                if max_dist[v] < max_dist[u] + weight:
                    max_dist[v] = max_dist[u] + weight
                    parent[v] = u
                    queue.append(v)

        # 最長パスの長さとその終点を見つける
        max_node = max(max_dist, key=max_dist.get)
        longest_path_length = max_dist[max_node]
        seen.add(max_node)
        # 最長パスを復元する
        while max_node is not None:
            max_node = parent[max_node]
            if max_node is None:
                break
            if len(G[max_node]) > 2:
                roots.append(max_node)
            seen.add(max_node)

        # print(s, seen, longest_path_length)

        return longest_path_length


    roots = deque()
    roots.append(0)

    while roots:
        root = roots.popleft()
        seen.add(root)
        # rootを根としたときに各辺からとれる最長パスを列挙
        for v, l in G[root]:
            if v in seen:
                continue
            # bfs
            score = (bfs(v) + l) * 2
            scores.append(score)
            # print(root, v, l, score)

    scores.sort(reverse=True)
    ans = list(accumulate(scores))
    ans += [ans[-1]] * (N - len(ans))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
