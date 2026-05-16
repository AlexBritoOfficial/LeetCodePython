"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


# n^2 due to slice
# def findMaxConsecutiveOnes(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#
#     i = 0
#     j = i + 1
#     max = 0
#
#     while i < len(nums) and j < len(nums):
#         if nums[i] == 1:
#             if nums[j] == 1:
#                 j += 1
#             else:
#                 if (len(nums[i:j]) > max):
#                     max = len(nums[i:j])
#                 i = j + 1
#                 j = i + 1
#         else:
#             i = j
#             j = i + 1
#
#     if len(nums[i:j]) > max and nums[i] != 0:
#         max = len(nums[i:j])
#
#     return max

# def findMaxConsecutiveOnes(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    max = 0
    i = 0
    j = 0

    while i < len(nums) and j < len(nums):

        if nums[i] == 1 and nums[j] == 1:
            j +=  1
            count += 1

        else:
            if (count > max):
                max = count
            i = j + 1
            j = i
            count = 0

    if count > max:
        max = count

    return max

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    maximum = 0

    for i in range(len(nums)):

        if nums[i] == 1:
            count += 1
        else:
            maximum = count
            count = 0

    return max(maximum, count)


if __name__ == "__main__":
    #nums = [1, 0, 1, 1, 0, 1]
    nums = [1, 1, 0, 1, 1, 1]
    # nums = [1]
    #nums = [1,1,0,1]
    #nums = [0, 0]
    print(findMaxConsecutiveOnes(nums))
