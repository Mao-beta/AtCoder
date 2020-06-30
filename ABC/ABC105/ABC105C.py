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


def main():
	N = NI()
	ans = ""
	while N != 0:
		if N % 2:
			ans += "1"
			N = (N-1) // (-2)
		else:
			ans += "0"
			N = N // (-2)
	if ans:
		print(ans[::-1])
	else:
		print(0)


if __name__ == "__main__":
	main()