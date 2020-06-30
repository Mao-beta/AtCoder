import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
	N = NI()
	R = [NLI() for _ in range(N)]
	B = [NLI() for _ in range(N)]
	R.sort(key= lambda x: x[1], reverse=True)
	B.sort(key= lambda x: x[0])
	ans = 0

	for b in B:
		for r in R:
			if r[0] < b[0] and r[1] < b[1]:
				ans += 1
				R.remove(r)
				break

	print(ans)


if __name__ == "__main__":
	main()