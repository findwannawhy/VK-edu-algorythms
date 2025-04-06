from itertools import combinations

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    
    # Находим максимальное произведение среди всех возможных комбинаций k элементов
    max_product = float('-inf')
    
    # Перебираем все возможные комбинации k элементов
    for comb in combinations(nums, k):
        curr_product = 1
        for num in comb:
            curr_product *= num
        max_product = max(max_product, curr_product)
    
    print(max_product)

if __name__ == "__main__":
    main() 