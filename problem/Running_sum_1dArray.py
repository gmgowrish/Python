def runningSum(nums):
    count = 0
    ans = []
    for i in range(len(nums)):
        count = nums[i] + count
        ans.append(count)
    print(ans)


runningSum([1, 2, 3, 4])
