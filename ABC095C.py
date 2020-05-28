A, B, C, X, Y = map(int, input().split())
c_max = max(X, Y) * 2
ans = float('inf')
for c in range(0, c_max+1, 2):
    a = X - c // 2
    b = Y - c // 2
    ans = min(max(a, 0)*A + max(b, 0)*B + c*C, ans)

print(ans)