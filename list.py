# # -- -- -- -- -- -- -- -- concatenation -- -- -- -- -- -- -- -- fir
#
# list1 = [1, 3, 4, 5]
# list2 = list1
# print(list1 is list2)
# list1 = list1 + [9]
# print(list1)
# print(list1 is list2)

# def expanding(l):
#     if len(l) < 3:
#         print(True)
#     for i in range(len(l) - 2):
#         diff = abs(l[i + 1] - l[i])
#         if diff >= abs(l[i + 2] - l[i + 1]):
#             print(False)
#     print(True)


# expanding([1, 3, 7, 2, 9])
#
#
# def sumsquare(l):
#     odd = 0
#     even = 0
#     for x in l:
#         if x % 2:
#             odd = odd + x ** 2
#         else:
#             even = even + x ** 2
#     return [odd, even]
#
#
# sumsquare([1, 3, 5])


# def transpose(m):
#     list1 = []
#     c = len(m[0])
#     r = len(m)
#
#     for i in range(0, c):
#         li = []
#         for j in range(0, r):
#             li = li + [m[j][i]]
#         list1 = list1 + [li]
#     return (list1)
#
#
# transpose([[1, 2, 3], [4, 5, 6]])
