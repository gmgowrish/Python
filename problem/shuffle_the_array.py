def shuffles(nums, n):
    ans = []
    xIndex = 0
    yIndex = n
    while xIndex < n and yIndex < 2 * n:
        ans.append(nums[xIndex])
        xIndex += 1
        ans.append(nums[yIndex])
        yIndex += 1
    print(ans)


shuffles([1, 2, 3, 4, 5, 6], 3)
