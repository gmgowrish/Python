def sumOfMaxMin(arr):
    mn = 0
    mx = 0
    for i in arr:
        if i > mx:
            mx = i
        elif i < mn:
            mn = i

    print(mn + mx)


sumOfMaxMin([2, 4, 5, 7, -1])
