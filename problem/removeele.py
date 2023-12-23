# nums = [3, 2, 2, 3]
#
# val = 3


# num = []
# uS = []
# for i in nums:
#     # print(i)
#     if nums[i] != val:
#         num.append(i)
#     else:
#         uS.append('_')
#
# # nums = [i for i in nums if nums[i] != val]
# print(num + uS)

# def removeEle(nums, val):
#     i = 0
#
#     for num in nums:
#         # print(nums)
#         if num != val:
#
#             nums[i] = num
#             i += 1
#         print(nums[i])
#
#     return i
#
#
# removeEle([3, 2, 2, 3], 3)

#
# haystack = 'hello'
#
# needle = "ll"
#
#
# print(haystack.index(needle))


nums = [1, 3, 5, 6]
target = [2]
gun = nums + target
print(sorted(gun.index(2)))
