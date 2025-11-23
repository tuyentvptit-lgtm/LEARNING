arr = list(map(int, input().split()))
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == 2* arr[j]:
            print('true')
            break
        else:
            print('false')