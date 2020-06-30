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
	querys = [NLI() for _ in range(M)]
	querys.sort(key=lambda x: x[1])
	ans = 0
	last = 0
	for a, b in querys:
		if a <= last < b:
			continue
		last = b-1
		ans += 1
	print(ans)


if __name__ == "__main__":
	main()