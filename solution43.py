def main():
    s = input().strip()
    hash_map = {}
    res = 0
    
    for char in s:
        hash_map[char] = hash_map.get(char, 0) + 1
        res = max(res, hash_map[char])
    
    print(res)
    return

if __name__ == "__main__":
    main() 