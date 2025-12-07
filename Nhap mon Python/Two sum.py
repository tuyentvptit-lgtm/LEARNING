nums = list(map(int, input().split()))
target = int(input())
cnt = []
for i in range(len(nums)):
    for j in range(i +1, len(nums)):
        if nums[i] + nums[j] == target:
            cnt.append(i)
            cnt.append(j)
            break
print(cnt)