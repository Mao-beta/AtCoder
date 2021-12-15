import math
import sys
from pathlib import Path
import random

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write("".join(map(str, row)) + "\n")
    else:
        for row in ans:
            print(*row)


def main():
    N = 400
    M = 1995

    dst_dir = Path("./in/")
    dst_dir.mkdir(exist_ok=True)

    XY = []

    for case in range(100):
        random.seed(case)
        filename = str(case).zfill(3) + ".in"

        lines = []
        for i in range(N):
            line = ""
            while True:
                x = random.randint(0, 800)
                y = random.randint(0, 800)
                min_d = 2000
                if not XY: break

                for xx, yy in XY:
                    min_d = min(min_d, math.sqrt((x-xx)**2 + (y-yy)**2))
                    if min_d <= 5:
                        break

                if min_d > 5:
                    break

            XY.append([x, y])
            line = f"{x} {y}"
            lines.append(line)



        output_ans(lines, dst_dir/filename)


if __name__ == "__main__":
    main()
