import bisect
N, K = map(int, input().split())
V = list(map(int, input().split()))
num_get = min(N, K)
ans = -float('inf')
for left in range(0, num_get+1):
    for right in range(N-1, N-1 - (num_get+1 - left), -1):
        inhand = sorted(V[0:left] + V[right+1:N])
        zero_idx = bisect.bisect_left(inhand, 0)
        tmp_ans = sum(inhand[min(zero_idx, max(K - len(inhand), 0)):])
        ans = max(ans, tmp_ans)
print(ans)