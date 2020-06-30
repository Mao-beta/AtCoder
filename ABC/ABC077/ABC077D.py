K = input()
keta = len(K)
K = int(K)
ans = 10000000000
for i in range(1, 10**keta):
    n = K * i
    kakui_sum = 0
    for j in range(100):
        kakui_sum += n % 10
        n = n // 10
        if n == 0:
            break

    print(str(K*i) + " " + str(kakui_sum))
    ans = min(ans, kakui_sum)

print(ans)