def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                # ans = nums[j]
                count += 1
        result.append(count)

    print(result)
    # sorted_nums = sorted(nums)
    # result = [sorted_nums.index(num) for num in nums]
    # print(result)


smallerNumbersThanCurrent([8, 1, 2, 2, 3])

'''  
 SOLUTION FOR THIS PROBLEM
 
result is the outer scope variable 

n= 5
i = 0 --> count = 0 
j = 0 --> 8 > 8 
      --> 8 > 1 , count = 1
      --> 8 > 2 , count = 2
      --> 8 > 2 , count = 3
      --> 8 > 3 , count = 4
      append(count) to result
i = 1 =[1] --> count = 0
j = 0 --> 1 > 8 
      --> 1 > 1
      --> 1 > 2
      --> 1 > 2
      --> 1 > 3
      append (count) to result = 0
      
i = 2 =[2]
j = 0 --> 2 > 8,
      --> 2 > 1 , count = 1
      --> 2 > 2,
      --> 2 > 2,
      --> 2 > 3,
      append (count) to result = 1
i = 4 = [3]
j = 0 --> 3 > 8 ,
      --> 3 > 1 , count = 1
      --> 3 > 2 , count = 2
      --> 3 > 2 , count = 3
      --> 3 > 3 ,
      append (count) to result = 3
      
finally print the result [4,0,1,1,3]

SECOND APPROACH

# sorted_nums = sorted(nums)
# result = [sorted_nums.index(num) for num in nums]
# print(result)
smallerNumbersThanCurrent([8, 1, 2, 2, 3])

------first step is to sort the given list ------
sorted(nums) --> [1,2,2,3,8]->(index ->[0,1,2,3,4])
-------second step is to iteration----------------
for nums in num:
    print(nums) # 1 2 2 3 8 
----------Accessing the looped index value this the final result------    
    print(num.index(nums)) # 0 1 1 3 4 
    



'''

num = [1, 2, 2, 3, 8]
for nums in num:
    # print(nums,end=' ')
    print(num.index(nums), end=' ')
