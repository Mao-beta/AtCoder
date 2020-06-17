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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
	N, M = NMI()
	Q = [NLI() for _ in range(M)]
	ans = 0
	for case in range(2**12):
		know = 0
		n = 0
		for i in range(12):
			n += (case >> i) & 1
		for x, y in Q:
			x -= 1
			y -= 1
			if ((case >> x) & 1) & ((case >> y) & 1):
				know += 1
		if know == n * (n-1) // 2:
			ans = max(ans, n)
	print(ans)


if __name__ == "__main__":
	main()