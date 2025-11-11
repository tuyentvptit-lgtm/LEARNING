arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] > arr[i - 1]:
        arr[i] = arr[i - 1], 
print (arr)