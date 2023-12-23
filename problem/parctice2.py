def permutations(nums):
    def backtrack(start):
        # print(start)
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result


# Test cases
print(permutations([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
print(permutations([0, 1]))  # Outnput: [[0, 1], [1, 0]]
print(permutations([1]))  # Output: [[1]]
