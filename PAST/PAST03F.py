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
	N = NI()
	S = [set(SI()) for _ in range(N)]
	ans = [""] * N

	if N == 1:
		print(list(S[0])[0])
		exit()

	for i in range(N):
		if i >= N / 2:
			break
		if N % 2 and i == (N-1) // 2:
			ans[i] = S[i].pop()
			continue

		if not S[i].intersection(S[N-1-i]):
			print(-1)
			exit()
		ans[i] = S[i].intersection(S[N-1-i]).pop()
		ans[N-1-i] = ans[i]

	ans = "".join(ans)
	print(ans if len(ans) == N else -1)


if __name__ == "__main__":
	main()