def twoSum(nums, target):

    numsDict = {}
    for i in range(len(nums)):
        difference = target - nums[i]

        if difference not in numsDict.values():
            numsDict[i] = nums[i]
        else:
            return [list(numsDict.values()).index(difference),i]


if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9

    nums = [3, 2, 4]
    target = 6

print(twoSum(nums, target))
