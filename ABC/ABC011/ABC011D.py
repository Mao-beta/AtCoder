import math

N, D = map(int, input().split())
X, Y = map(int, input().split())
if X % D or Y % D:
    print(0.0)
    exit()

X = abs(X // D)
Y = abs(Y // D)

# R:X+i L:i U:Y+j D:j -> N
# X+Y+2i+2j == N
# N-X-Y :even

if (N - X - Y) % 2:
    print(0.0)
    exit()

ans = 0
limit = (N-X-Y)//2
for i in range(limit+1):
    j = limit - i
    ans += math.factorial(N) // math.factorial(X+i) // math.factorial(i) // math.factorial(Y+j) // math.factorial(j)

ans = ans / 4**N
print(ans)