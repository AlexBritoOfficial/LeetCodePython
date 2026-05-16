def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    i = 0
    while i < (len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

        i += 1

    return k


if __name__ == "__main__":
    nums = [3,2,2,3]
    removeElement(nums, 3)