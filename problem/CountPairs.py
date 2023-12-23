def countPairs(nums, target):
    count = 0
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                count += 1

    print(count)


countPairs([-1,1,2,3,1], 2)
