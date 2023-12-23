def twosum(nums, target):
    index_map = {}
    # print(index_map)
    for index, num in enumerate(nums):
        print(index)
        # print(num)
        if target - num in index_map:
            # print(target - num)
            # print(index_map)
            print( index_map[target - num], index)
        index_map[num] = index
    # print(index_map)


a = [2, 7, 11, 15, 9]
twosum(a, 9)
