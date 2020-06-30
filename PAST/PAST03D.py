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
	S = [SI() for _ in range(5)]
	idx_left = [i*4 for i in range(N)]
	digits = []
	S_digit = [
		".###..#..###.###.#.#.###.###.###.###.###.",
		".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.",
		".#.#..#..###.###.###.###.###...#.###.###.",
		".#.#..#..#.....#...#...#.#.#...#.#.#...#.",
		".###.###.###.###...#.###.###...#.###.###."
	]
	idx_digit = [i * 4 for i in range(10)]
	for start in idx_digit:
		stop = start + 4
		now = [S_digit[i][start:stop] for i in range(5)]
		digits.append(now)

	ans = ""
	for start in idx_left:
		stop = start + 4
		now = [S[i][start:stop] for i in range(5)]
		for i, d in enumerate(digits):
			if now == d:
				ans += str(i)
				break
	print(ans)


if __name__ == "__main__":
	main()