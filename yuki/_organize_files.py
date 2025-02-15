import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
import re
from pathlib import Path

sys.set_int_max_str_digits(10 ** 6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]

def organize_files():
    current_dir = Path(".")
    pattern = re.compile(r"^yuki_(\d{4})\.py$")  # Match "yuki_" followed by exactly 4 digits and ".py"
    for file in current_dir.iterdir():
        if file.is_file():
            match = pattern.match(file.name)
            if match:  # Check if regex matched and extracted digits
                number = int(match.group(1))
                folder = current_dir / f"{number // 100:02d}xx"  # Calculate folder name
                folder.mkdir(exist_ok=True)  # Create folder if it doesn't exist
                file.rename(folder / file.name)  # Move file to folder


def main():
    organize_files()


if __name__ == "__main__":
    main()
