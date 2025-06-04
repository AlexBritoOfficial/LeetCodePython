from ctypes import c_int
from operator import truediv


def containsDuplicate(nums):

    numsDict  = dict()

    for i in range(len(nums)):
        count = 0
        if nums[i] in numsDict:
            return True
        else:
           numsDict[nums[i]] = count + 1
    return False

if __name__ == "__main__":

    nums = [1,2,3,1]
    print(containsDuplicate(nums))



