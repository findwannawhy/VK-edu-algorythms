def q_sort(nums, start, end):
    if start >= end:
        return
    
    i, j = start, end
    pivot = nums[(start + end) // 2]
    
    while i <= j:
        while i <= end and nums[i] < pivot:
            i += 1
        while j >= start and nums[j] > pivot:
            j -= 1
            
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    q_sort(nums, start, j)
    q_sort(nums, i, end)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    q_sort(nums, 0, n-1)
    
    print(" ".join(map(str, nums)))

if __name__ == "__main__":
    main() 