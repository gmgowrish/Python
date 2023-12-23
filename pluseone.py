digits = [1, 3, 4]
# num2 = 0
# num = []
# for i in digits:
#     num2 = num2 * 10 + i
#
#
#     num.append(i)
#
# print(num2 )
# print(num)


# for x in digits:


# for i in digits:
#     number = number * 10 + i
#     print(number)
#
# num = number + 1
# add1 = str(num)
#
# sub = ''.join(add1)
#
# print(list(sub))
def plusOne( digits):
    return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]
plusOne[1,2,3]