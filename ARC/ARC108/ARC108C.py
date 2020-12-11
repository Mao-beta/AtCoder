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


#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append((edge[1], edge[2]))
        res[edge[1]].append((edge[0], edge[2]))
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = make_adjlist_nond(N, edges)
    nums = [0] * (N+1)

    stack = deque()
    stack.append(1)
    nums[1] = 1

    while stack:
        now = stack.popleft()
        now_num = nums[now]
        #print("now: ", now)
        for goto, label in graph[now]:
            if nums[goto] != 0: continue
            #print("goto: ", goto)
            if label == now_num:
                if now_num == 1:
                    next_num = 2
                else:
                    next_num = 1
            else:
                next_num = label

            nums[goto] = next_num
            #print(f"point{goto} num{next_num}")
            stack.append(goto)

    for n in nums[1:]:
        print(n)


if __name__ == "__main__":
    main()
