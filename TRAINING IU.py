nums = list(map(int, input().split()))
k = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]
        k += 1
    print(k)
    print(nums)