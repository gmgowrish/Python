def goodPairs(nums):
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    print(count)


goodPairs([1, 2, 3, 1, 1, 3])


def lenog(n):
    print(len(n))


lenog([1, 2, 3, 1, 1, 3])
