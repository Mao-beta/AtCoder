# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest
import sys
from cp_snippet_palette.library.structures.wavelet_matrix import WaveletMatrix


def main():
    read = sys.stdin.buffer.readline
    n, q = map(int, read().split())
    wm = WaveletMatrix(list(map(int, read().split())))
    answer = [str(wm.kth_smallest(*map(int, read().split()))) for _ in range(q)]
    print("\n".join(answer))


if __name__ == "__main__":
    main()
