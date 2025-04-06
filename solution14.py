n = int(input())
nums = list(map(int, input().split()))

res = nums[0]
for el in nums:
    if el > res:
        res = el

print(res)