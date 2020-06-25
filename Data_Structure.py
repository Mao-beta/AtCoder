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


# SegTreeの関数
def segfunc(x, y):
	return min(x, y)
# 単位元
# min->inf, max->-inf, add->0, mul->1
ide_ele = float("inf")

# セグメント木
class SegTree:
	"""
	init(init_val, segfunc, ide_ele): 配列init_valで初期化、構築
	update(k, x): k番目の値をxに更新
	query(l, r): 区間[l, r)をsegfuncしたものを返す
	"""
	def __init__(self, init_val, segfunc, ide_ele):
		n = len(init_val)
		self.segfunc = segfunc
		self.ide_ele = ide_ele
		self.num = 1 << (n-1).bit_length()




def main():
	pass


if __name__ == "__main__":
	main()