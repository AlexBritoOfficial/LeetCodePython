def containsNearbyDuplicate(nums, k):

    dict = {}
    for i in range(len(nums)):

        if nums[i] in dict:
           current_list = dict[nums[i]]
           if abs(current_list[0] - i) <= k:
               return True
           else:
               dict[nums[i]] = [i]

        else:
            dict[nums[i]] = [i]
    return False

if __name__ == "__main__":
    nums = [1,0,1,1]
    k = 1
    print(containsNearbyDuplicate(nums, k))