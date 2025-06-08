from operator import index


def searchInsert(nums, target):
    return searchInsertHelper(nums, 0, len(nums), target)


def searchInsertHelper(nums, left, right, target):
    mid = (left + right) // 2

    if left >= right:
        return left

    if target < nums[mid]:
        return searchInsertHelper(nums, left, mid, target)

    elif target > nums[mid]:
        return searchInsertHelper(nums, mid + 1, right, target)

    else:
        return mid


if __name__ == "__main__":
    nums = [1, 3, 5, 6]

    print(searchInsert(nums, 7))
