import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()



def main():
    N = NI()

    graph = [[] for _ in range(2*N-1)]
    for i in range(N-1):
        u, v = NMI()
        u, v = u-1, v-1
        t = i + N
        graph[u].append(t)
        graph[v].append(t)
        graph[t].append(u)
        graph[t].append(v)

    if N == 2:
        print(1)
        exit()

    def steps(start, seen):
        stack = deque()
        stack.append(start)
        seen[start] = 0

        while stack:
            now = stack.pop()
            now_step = seen[now]
            for goto in graph[now]:
                if seen[goto] >= 0:
                    continue
                stack.append(goto)
                seen[goto] = now_step + 1

        return seen

    S = steps(0, [-1]*(2*N-1))
    D = max(S)
    root1 = S.index(D)

    SR = steps(root1, [-1]*(2*N-1))
    D = max(SR)
    root2 = SR.index(D)

    SR2 = steps(root2, [-1]*(2*N-1))

    d = D // 2
    for i, (x, y) in enumerate(zip(SR, SR2)):
        if x == y == d:
            center = i
            break
    seen = [-1] * (2*N-1)
    seen[center] = 0

    def dfs_stack(start):
        stack = deque()
        stack.append((start, -1))
        nums = []
        num = 0

        while stack:
            now, par = stack.pop()
            now_step = seen[now]

            if now_step == d:
                num += 1
                continue

            for goto in graph[now]:
                if seen[goto] >= 0:
                    continue
                seen[goto] = now_step + 1
                stack.append((goto, now))

            if par == start:
                nums.append(num)
                num = 0

        nums.append(num)
        return nums


    nums = dfs_stack(center)
    ans = 1
    for num in nums:
        ans = (ans * (num+1)) % MOD
    ans = (ans - 1 - sum(nums)) % MOD

    print(ans)


if __name__ == "__main__":
    main()
