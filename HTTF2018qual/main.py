import sys
import random
import time

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def read_input_file(path):
    """
    pathのファイルをNLI()形式などでよみこむ
    """
    with open(path, mode="r") as f:
        A = [list(map(int, l.split())) for l in f.readlines()]
    return A


def add_mt(grid, x, y, h):
    N = 100
    for nx in range(N):
        for ny in range(N):
            grid[ny][nx] += max(0, h - abs(y-ny) - abs(x-nx))

    return grid


def add_mt_fast(grid, x, y, h, A):
    N = 100
    add_score = 0
    for nx in range(x-h, x+h+1):
        gx = abs(x - nx)
        gy = h - gx
        for ny in range(y-gy, y+gy+1):
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            base_gap = abs(A[ny][nx] - grid[ny][nx])
            grid[ny][nx] += h - abs(y - ny) - abs(x - nx)
            new_gap = abs(A[ny][nx] - grid[ny][nx])
            add_score += new_gap - base_gap

    return add_score


def del_mt(grid, x, y, h):
    N = 100
    for nx in range(N):
        for ny in range(N):
            grid[ny][nx] -= max(0, h - abs(y-ny) - abs(x-nx))

    return grid


def del_mt_fast(grid, x, y, h, A):
    N = 100
    add_score = 0
    for nx in range(x - h, x + h + 1):
        gx = abs(x - nx)
        gy = h - gx
        for ny in range(y - gy, y + gy + 1):
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            base_gap = abs(A[ny][nx] - grid[ny][nx])
            grid[ny][nx] -= h - abs(y - ny) - abs(x - nx)
            new_gap = abs(A[ny][nx] - grid[ny][nx])
            add_score += new_gap - base_gap

    return add_score


def calc_gap(A, B):
    N = 100
    res = 0
    for y in range(N):
        for x in range(N):
            res += abs(A[y][x] - B[y][x])
    return res


def main():
    start_time = time.time()
    TIME_LIMIT = 5.8

    try:
        import numpy
        is_local = True
    except:
        is_local = False

    N = 100

    if is_local:
        path = "./in/example_01.txt"
        A = read_input_file(path)
    else:
        A = [NLI() for _ in range(N)]

    B = [[0]*N for _ in range(N)]

    random.seed(12)
    XYH = []
    gap = sum([sum(r) for r in A])
    for i in range(1000):
        x = random.randint(0, N-1)
        y = random.randint(0, N-1)
        h = random.randint(1, N)
        gap += add_mt_fast(B, x, y, h, A)
        XYH.append([x, y, h])

    #print(gap)
    cnt = 0
    while True:
        new_gap = gap
        del_idx = random.randint(0, N-1)
        dx, dy, dh = XYH[del_idx]
        new_gap += del_mt_fast(B, dx, dy, dh, A)

        x = random.randint(0, N-1)
        y = random.randint(0, N-1)
        h = random.randint(1, N)
        new_gap += add_mt_fast(B, x, y, h, A)

        if new_gap < gap:
            gap = new_gap
            XYH[del_idx][0] = x
            XYH[del_idx][1] = y
            XYH[del_idx][2] = h
            cnt += 1
            #print(cnt, gap)
        else:
            del_mt_fast(B, x, y, h, A)
            add_mt_fast(B, dx, dy, dh, A)

        if time.time() - start_time > TIME_LIMIT:
            break

    print(len(XYH))
    for x, y, h in XYH:
        print(x, y, h)
        pass


if __name__ == "__main__":
    main()
