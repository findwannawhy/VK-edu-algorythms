def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    
    l = 0
    r = n - 1
    
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            print(mid)
            return
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    if r < 0:
        print(0)
    elif target > nums[r]:
        print(r + 1)
    else:
        print(r)

if __name__ == "__main__":
    main()