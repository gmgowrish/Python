# list1 = [0, 1, 2]
# for i in range(3):
#     if list1 == i:
#         print(True)
#     else:
#         print(False)
#
# nums = [1, 2, 3, ]
#
# for i in range(0, len(nums), 2):
#     print(i)
#
# print([3] * 2)
#

def find_missing_number_xor(nums):
    len_n = len(nums)
    res = len_n
    print(res)

    for i in range(len_n):
        res += i - nums[i]
    return res


# Example usage:
nums = [ 0, 1]
result = find_missing_number_xor(nums)
print(result)

''' 
                  9
0 - 9 = -9 + 1 = -8
1 - 6 = -5 + 1 = -4
2 - 4 = -2 + 1 = -1
3 - 2 =  1 + 1 =  2
4 - 3 =  1 + 1 =  2
5 - 5 =  0 + 1 =  1
6 - 7 = -1 + 1 =  0
7 - 0 =  7 + 1 =  8
8 - 1 =  7 + 1 =  8


ints = range(0, len(nums) + 1)
print(set(ints).difference(nums).pop())
print()
return set(ints).difference(nums).pop()
    
    
    
'''
