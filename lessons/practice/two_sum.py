"""
    Two Sum
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

    Source: LeetCode
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)

        if size < 2:
            print('Input array must contain at least two integers')
            return

        for i in range(size-1):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]

        print('No solution exists')

if __name__ == '__main__':
    test = Solution()

    #Test 0: From example above
    nums = [2, 7, 11, 15]
    target = 9
    print('\nTest 0')
    print(test.twoSum(nums, target))

    # Test 1: Input array with less than two integers
    nums = [1]
    target = 10
    print('\nTest 1')
    print(test.twoSum(nums, target))

    #Test 2: Input array with two integers and a solution
    nums = [7, 5]
    target = 12
    print('\nTest 2')
    print(test.twoSum(nums, target))

    #Test 3: Input array with two integers and no solution
    nums = [1, 5]
    target = 12
    print('\nTest 3')
    print(test.twoSum(nums, target))

    #Test 4: Input array with more than two integers
    nums = [9, 4, 7, 21, 1, 33]
    print('\nTest 4')
    target = 13
    print(test.twoSum(nums, target))
    target = 34
    print(test.twoSum(nums, target))
    target = 30
    print(test.twoSum(nums, target))
    target = 54
    print(test.twoSum(nums, target))
    target = 42
    print(test.twoSum(nums, target))
    target = 28
    print(test.twoSum(nums, target))
    target = 5
    print(test.twoSum(nums, target))
    target = 0
    print(test.twoSum(nums, target))
