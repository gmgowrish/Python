# keys = ['navin', 'gmg', 'dilip']
# values = ['python', 'java', 'js']
# # print(type(keys))
# data = dict(zip(keys, values))
# data['monika'] = 'cs'
# # print(type(data))
# del data['navin']
#
# porg = {'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'subline']}
# # print(type(porg))
# # print(porg)
# # print(porg['python'])
# # more on variables
# num = 5
# # print(num)
# a = 10
# b = a
# # print(type(a))
# # print(b)
# data1 = id(a)
# data2 = id(b)
# # print(data1)
# # print(data2)
#
# nums = 6 + 9j
# # print(type(nums))
# # converting one data type to other
# a = 5.6
# b = int(a)
# # print(type(b))
# k = float(b)
# # print(k)
# c = complex(a, k)
# # print(c)
# a = k < b
# # print(type(a))
# str = "gmggowrish"
# # print(type(str))
#
# # print(list(range(10)))
# d = {'gmg': 'oppo', 'dilip': "samsung", 'arun': 'viv0'}
# print(d)
# print(d.keys())
# print(d.values())
# #  operators
# x = 10
# x *= 10
# print(x)
# x -= 10
# print(x)
# a, b = 10, 20
# print(a)
# print(b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < 8 and b < 5)
# print(a < 8 or b < 5)
# # print(a not a)
# print(bin(25))  # bin ,oct dec hex
# print(0b11001)  # 0b Represents the binary number
# # swapping two number
# a = 10
# b = 20
# # temp= a
# # a=b
# # b=temp
# # a=a+b
# # b=a-b
# # a=a-b
# a, b = b, a
# print(a)
# print(b)
# # bit wise oprator
#
# print(~12)
# print(12 & 13)
# print(12 | 13)
# print(12 ^ 14)
# print()
# import math as m
#
# x = m.sqrt(25)
# print(x)
# print(m.floor(x))
# print(m.ceil(3.1))
#
# # Get the input from the user by using keyword input()
# # x = int(input("say something:"))  # integer
# # y = int(input("say something:"))
# # z = x / y
# # print(m.ceil(z))
#
# # x = input("enter your fucking name🍑:")
# # y = input("enter your full name bitch🎆:")
# # print((x + y) + "thank u bitch-_-")
#
# # result = eval(input("enter fucking expression"))
# # print(result)
# # if elif else statements
# x = 10
# r = x % 2
# if r == 0:
#     print("i am good boy")
#     if r < 0:
#         print("fuck u tony")
#     else:
#         print("get out my laptop")
# else:
#     print("chithiya")
# print("bye")
#
# z = 5
# if z == 1:
#     print("one")
# elif z == 2:
#     print("two")
# elif z == 3:
#     print("three")
# elif z == 4:
#     print("four")
# else:
#     print("opps🤦‍♂️try again")
# #     loop
# i = 1
#
# while i <= 4:
#     print(" # ",
#           end="")  # end used print on same line gmg  Good Morning Gowrish Good Morning Gowrish Good Morning Gowrish Good Morning Gowrish
#     # gmg
#     # gmg
#     # gmg
#     # gmg
#     j = 1
#     while j <= 3:
#         print(" # ", end="")
#         j = j + 1
#     i = i + 1
#     print()
# k = 1
# # while k <= 1:
# # print(k)
# # k = k + 1
# a = 1
# while a <= 100:
#     print(a)
#     a = a + 5
# # for loop
# x = ['navin', 2, 6.0]
# for i in x:
#     print(i)
#
# for i in range(0, 10):  # for inside if loop
#     if i % 5 != 0:
#         print(i)
# # for Square number b/t 1 and 50
# for i in range(1, 51):
#     z = i * i
#     print(z)
#
# # Break statement
#
# av = 5
#
# # x = int(input("How Many Girls  You Wants"))
# # i = 1
# # while i <= x:
# #     if i > av:
# #         print("out of stock")
# #         break
# #
# #     print(i)
# #     i += 1
# # print("we have only girls")
# # continue
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         continue
#     # print(i)
# print("byeeeeeeeeeee")
#
# # pass
# for i in range(1, 100):
#
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)
# # odd number
# for i in range(2, 100):
#     if i % 100 == 0:
#         print(i)
#  pass continue break


#  pattern1
#  #  #  #  #
#  #  #  #  #
#  #  #  #  #
#  #  #  #  #
#  #  #  #  #

# for i in range(5):
#     for j in range(5):
#         print(" # ", end="")
#     print()

#  pattern2
#  #  #  #  #
#  #  #  #
#  #  #
#  #
#

# for i in range(5):
#     for j in range(i, 5):
#         print(" # ", end="")
#     print()

#  pattern3
#
#  #
#  #  #
#  #  #  #
#  #  #  #  #
# method 1
# for i in range(5):
#     for j in range(-1, i):
#         print(" # ", end="")
#     print()
#
# #     method 2
# for i in range(5):
#     for j in range(i+1):
#         print(" (●ˇ∀ˇ●) ", end="")
#     print()

#  for else
# nums = [13, 14, 16, 18]
# for i in nums:
#     if i % 5 == 0:
#         print(i)
#         break
# else:
#     print("not found")
# break
# prime number
# x = int(input("Enter the number to be checked for prime: "))
# for i in range(2, x):
#     if x % i == 0:
#         print(x, "is not a prime number")
#         break
# else:
#     print(x, "is a prime number")
# from array import *

# vals = array('i', [5, 6, 8, 5, ])
# print(vals.buffer_info())
# # output  (1627992348752, 6) address number element in array
# for i in range(len(vals)):
#     print(vals[i])
#
# newarray = array(vals.typecode, (a * a for a in vals))
# for i in newarray:
#     print(i)
#
# e = 0
# while e < len(newarray):
#     print(newarray[e])
#     e += 1

# array value from user

# arr = array('i', [])
#
# n = int(input("enter the length of an array"))
#
# for i in range(n):
#     x = int(input("enter the element:"))
#     arr.append(x)
# print(arr)
#
# val = int(input("Enter the values for search!"))
#
# k = 0
# for e in arr:
#     if e == val:
#         print(k)
#         break
#     k += 1
#
# print(arr.index(val))

from numpy import *

# arr = array([1, 2, 5, 3])
# print(arr.dtype)
# print(arr)
#
# # coping array to another
#
# arr2 = arr.copy()
# print(arr2)
# arr3 = arr2 + arr
# print(max(arr3))
# print(id(arr))
# print(id(arr2))
#
# # shallow copy
# arr2[1] = 7
# print(arr)
# print(arr2)


# multidimensional array

arr1 = matrix('1 2 3; 4 2 4; 5 3 5; 6 7 9; 2 4 5 ')
# arr2 = arr1.flatten()
#
# arr3 = arr2.reshape(2, 2)
print(arr1)

# Program to multiply two matrices (vectorized implementation)

# Program to multiply two matrices (vectorized implementation)
import numpy as np

# take a 3x3 matrix
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x4 matrix
B = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

# result will be 3x4

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

result = np.dot(A, B)

for r in result:
    print(r)
