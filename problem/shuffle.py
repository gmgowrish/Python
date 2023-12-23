def Difference(nums1, nums2):
    temp = []
    temp1 = []
    for i in nums1:
        if i not in nums2:
            temp.append(i)

    print(temp)
    for j in nums2:
        if j not in nums1:
            temp1.append(j)
    print(temp1)

    print([temp, temp1])


Difference([4, 5, 6], [2, 3, 4])
# 2215
