length = int(input())
inputList = list(map(int, input().split()))
element = int(input())
arr = []
index = 0

for i in range (length):
    if (inputList[i] != element):
        arr.append(inputList[i])

print(*arr)