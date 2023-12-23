def zeroToLast(nums):
    zero = []
    num = []
    for i in range(0, len(nums)):
        if nums[i] == 0:
            zero1 = nums[i]
            zero.append(zero1)
        else:
            num1 = nums[i]
            num.append(num1)
    # print(zero)
    print(num + zero)


zeroToLast([0, 1, 0, 3, 12])
