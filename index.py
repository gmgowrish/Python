# def isPalindrome(x):
#     x_str = str(x)
#     return x_str
#
#
# print(isPalindrome(121))

# #
# # x = 121
# # d = list[x]
# # a = split(d)
# #
# # print(d)
#
# num =-1
#
# num = num - 5
#
# print(num)
#
# def maxProfit(prices):
#     if not prices:
#         return 0
#
#     max_profit = 0
#     min_price = prices[0]
#
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#
#     return max_profit
h = [1, 2, 3, 4, ]


# d = set(h)
# if h == d:
#     print("True")
# else:
#     print("False")

# n=len(h)

#
# for i in h:
#     if i < (i + 1):
#         print()
#     else:
#         print("not")
# print("sorted")
# def patter(n):
#     k = 1
#     for i in range(1, 10):
#
#         for j in range(1, i+1):
#             print(k, end='')
#             K += 1
#
#         print("")


def floydTriangle(n):
    val = 1
    for i in range(1, n + 1):

        for j in range(1, i + 1):
            print(val, end=" ")
            val += 1

        print("")


floydTriangle(4)
