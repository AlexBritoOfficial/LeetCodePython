from enum import unique


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int"""


    uni = 0
    for i in range(len(nums)):
        uni = uni ^ nums[i]

    return uni

if __name__ == "__main__":
    # nums = [2,2,1]
    nums = [4, 1, 2, 1, 2]
    print(singleNumber(nums=nums))
