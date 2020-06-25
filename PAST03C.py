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
	A, R, N = NMI()
	if R == 1:
		print(A)
		exit()
	if N >= 31:
		print("large")
		exit()
	ans = A
	for i in range(N-1):
		ans *= R
		if ans > 10**9:
			print("large")
			exit()
	print(ans)


if __name__ == "__main__":
	main()