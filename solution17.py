n = int(input())
nums = list(map(int, input().split()))

res = -1
for el in nums:
    if el % 2 == 0:
        res = el

print(res)