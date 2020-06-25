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


#隣接リスト 1-order
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
	N, M, Q = NMI()
	edges = [NLI() for _ in range(M)]
	colors = [-1] + NLI()
	querys = [NLI() for _ in range(Q)]
	adj = make_adjlist_nond(N, edges)

	for query in querys:
		if query[0] == 1:
			x = query[1]
			print(colors[x])
			for a in adj[x]:
				colors[a] = colors[x]
			continue

		x, y = query[1], query[2]
		print(colors[x])
		colors[x] = y


if __name__ == "__main__":
	main()