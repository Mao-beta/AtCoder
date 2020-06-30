A, B, N = map(int, input().split())
if N < B:
    ans = A * N // B - N // B * A
else:
    ans = A * (B-1) // B - (B-1) // B * A
print(ans)