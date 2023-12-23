a = [1, 0, 3, 5]


def sumIndices(nums, k):
    summ = 0
    for i in range(len(nums)):
        print(nums.bit_count())

        if i.bit_count() == k:

            summ += nums[i]
            # print(nums[i])
    # print(summ)


sumIndices([4, 3, 2, 1], 2)
