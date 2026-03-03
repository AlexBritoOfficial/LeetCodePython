
def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    concatenated = [None] * (len(nums) * 2)
    for i in range(len(nums)):
        concatenated[i], concatenated[len(nums) + i] = nums[i], nums[i]

    return concatenated





if __name__ == "__main__":
    nums = [1,2,1]
    print(getConcatenation(nums))







