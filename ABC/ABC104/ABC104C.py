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
	D, G = NMI()
	problems = [NLI() for _ in range(D)]
	n = D
	ans = 10**10
	for case in range(2 ** n):
		res = 0
		point = 0
		maxbit = 0
		for i in range(n):
			if (case >> i) & 1:
				res += problems[i][0]
				point += problems[i][1] + problems[i][0] * (i+1) * 100
			else:
				maxbit = max(maxbit, i)
				pass

		if point >= G:
			ans = min(ans, res)
			continue

		for i in range(problems[maxbit][0]):
			point += (maxbit+1) * 100
			res += 1
			if point >= G:
				ans = min(ans, res)
				break

	print(ans)


if __name__ == "__main__":
	main()