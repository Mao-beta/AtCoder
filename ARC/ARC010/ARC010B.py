N = int(input())
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_cum = [0, 0]
for month in months:
    months_cum.append(months_cum[-1] + month)

holidays = []
for i in range(N):
    m, d = map(int, input().split("/"))
    holidays.append(months_cum[m] + d)

calendar = ["0"] * 367
cnt = 0
for day, code in enumerate(calendar):
    if day == 0:
        continue
    if day % 7 <= 1:
        cnt += 1
    if day in holidays:
        cnt += 1
    if cnt >= 1:
        calendar[day] = "1"
        cnt -= 1

calendar = str("".join(calendar)).split("0")
ans = 0
for c in calendar:
    ans = max(ans, len(c))
print(ans)