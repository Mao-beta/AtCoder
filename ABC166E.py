N = int(input())
A = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
for i, a in enumerate(A):
    i = i+1
    if i+a <= N:
        left[i+a] += 1
    if i-a >= 1:
        right[i-a] += 1
ans = 0
for l, r in zip(left, right):
    ans += l * r
print(ans)