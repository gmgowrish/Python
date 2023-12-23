def differenceOfSum(_4):
    print("hello")
    # a, b = sum(nums), 0
    # for x in nums:
    #     while x:
    #         b += x % 10
    #         x //= 10
    # print(abs(a - b))
    e = 0

    for i in _4:
        # print(i)
        e += i
        for j in str(i):
            e -= int(j)
    print(abs(e))


_4 = [1, 15, 6, 3]
differenceOfSum(_4)
