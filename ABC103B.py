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
	S = deque(SI())
	T = deque(SI())
	for i in range(len(S)):
		S.rotate(1)
		if T == S:
			print('Yes')
			exit()
	print('No')



if __name__ == "__main__":
	main()