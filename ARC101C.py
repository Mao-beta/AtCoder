N, K = map(int, input().split())
x = list(map(int, input().split()))
N_minus = len([m for m in x if m < 0])
ans = float('inf')

for i in range(N):
    left = i
    right = i + K - 1
    if right >= N:
        break

    if x[right] <= 0:
        ans = min(x[left] * (-1), ans)
    elif x[left] < 0:
        ans = min(x[left] * (-1) * 2 + x[right], ans)
        ans = min(x[left] * (-1) + x[right] * 2, ans)
    else:
        ans = min(x[right], ans)

print(ans)