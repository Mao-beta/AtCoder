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
	A, B, C, D, E, F = NMI()
	W = []
	for i in range(31):
		for j in range(16):
			if 0 < (A*i + B*j) * 100 <= F:
				W.append(A*i + B*j)
	W = set(W)
	S = set()
	for i in range(3001):
		if C*i > 30 * E:
			break
		for j in range(1501):
			if 0 < C*i + D*j <= 30 * E:
				S.add(C*i + D*j)
	con = 0
	ans = [100*A, 0]
	for w in W:
		for s in S:
			if s <= F - 100 * w and s <= w * E and 100 * s / w >= con:
				con = 100 * s / w
				ans = [100*w + s, s]
	print(ans[0], ans[1])



if __name__ == "__main__":
	main()