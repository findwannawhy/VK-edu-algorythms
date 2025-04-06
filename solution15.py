n = int(input())
nums = list(map(int, input().split()))

min_diff = nums[1] - nums[0]
l = 0

for i in range(len(nums) - 1):
    if nums[i + 1] - nums[i] < min_diff:
        min_diff = nums[i + 1] - nums[i]
        l = i

print(nums[l], nums[l + 1])