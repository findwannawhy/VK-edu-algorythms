def main():
    n = int(input())
    nums = list(map(int, input().split()))
    hash_map = {}
    
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
        if hash_map[num] > n/2:
            print(num)
            return
    
    print(-1)
    return

if __name__ == "__main__":
    main() 