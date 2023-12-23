from array import *

nums = array('i', [1, 2, 3, 4, 5, ])
nums.append(12)
nums.remove(4)
print(nums.typecode)
print(nums.buffer_info())

# Inserting the value to the array
# arr = array('i', [])
#
# n = int(input("Enter the number of values "))
#
# for i in range(n):
#     x = int(input(f"enter {i}th number "))
#     arr.append(x)
# print(arr)
#
# # Selecting the index for given array
# idx = 0
#
# for ele in arr:
#     if ele == -5:
#         print(idx)
#         break
#     idx += 1
#
# #   Using the index function
# print(arr.index(-5))

# Using the Numpy for 2D matrix

from numpy import *

print("----Numpy----")
vals = array([[1, 2, 3],
              [4, 5, 6]], float)
print(vals)

# Linspace
print("--linspace--")
vals = linspace(0, 1, 5)

print(vals)

# logspace
print("-----logspace-----")
vals = logspace(1, 40, 5)
print(vals[4])
print('%.2f' % vals[4])

# arange
print("----arange----")
vals = arange(1, 20, 3)
print(vals)

# Zeros and one's
print("--Zeros--")
vals = zeros(4)
print(vals)

print("--ones--")
vals = ones(4)
print(vals)

#  Mathematical function
print("-------------mathematical operations --------------")
arr1 = array([[1, 2, 3],
              [3, 4, 5]])
arr2 = array([[4, 5, 6],
              [7, 5, 4]])

print(arr1 ** arr2)
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 // arr2)
print(arr1 % arr2)

print(concatenate([arr1, arr2]))

#  Creating the copy of the array

arra1 = array([1, 2, 3])


# Shallow copy
print("----------Shallow Copy---------")
arra2 = arra1.view()
print(id(arra1))
print(id(arra2))

print(arra1)
print(arra2)

arra1[2] = 6
print(arra2)


# Deep copy

arr3 = arra1.copy()

print("----------Deep Copy -------------")
print(arra1)
print(arr3)

arra1[1] = 5
print(arra1)
print(arr3)