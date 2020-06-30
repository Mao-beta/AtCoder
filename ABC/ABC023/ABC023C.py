import sys
import collections


input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    R, C, K = NMI()
    N = NI()
    candies = [NLI() for _ in range(N)]

    rows = [0] * (R+1)
    columns = [0] * (C+1)
    grid = {}
    for candy in candies:
        r, c = candy
        rows[r] += 1
        columns[c] += 1
        grid[1000000 * r + c] = 1
    rows_cnt = collections.Counter(rows)
    cols_cnt = collections.Counter(columns)
    rows_cnt[0] -= 1
    cols_cnt[0] -= 1

    ans_K = 0
    for i in range(K+1):
        ans_K += rows_cnt[i] * cols_cnt[K - i]
    for candy in grid:
        r = candy // 1000000
        c = candy % 1000000
        if rows[r] + columns[c] == K:
            ans_K -= 1
        if rows[r] + columns[c] == K + 1:
            ans_K += 1
    print(ans_K)


if __name__ == "__main__":
    main()