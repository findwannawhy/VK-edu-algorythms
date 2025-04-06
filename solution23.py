def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    border = 1
    last = n - 1

    while border < last and nums[border] < target:
        if nums[border] == target:
            print(border, border * 2)
            return
        border = border * 2
        if border > last:
            print(border // 2, border)
            return
    
    print(border // 2, border)
    return

if __name__ == "__main__":
    main() 