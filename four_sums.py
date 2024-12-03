def four_sums(nums,val):
    nums.sort()
    res, quad = [], []

    def kSum(k, start, target):

        if k != 2:
            for i in range(start, len(nums) - k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(k-1, i+1, target - nums[i])
                quad.pop()
            return
        
        l, r = start, len(nums) - 1
        while l < r:
           
            if nums[l] + nums[r] > target:
                l += 1
            elif nums[l] + nums[r] < target:
                r -= 1

            else:
                res.append(quad, [nums[l] + nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    # kSum(4,0,target)
    return res


         





# def twoSum_brute_force(nums, target):
#   """
#   Finds the first pair of integers in an array that sum to a given target value using brute force.

#   Args:
#       nums: A list of integers.
#       target: The target sum value.

#   Returns:
#       A list containing the indices of the two numbers if found, otherwise [-1, -1].
#   """
  
#   n = len(nums)
#   for i in range(n):
#     for j in range(i + 1, n):
#       if nums[i] + nums[j] == target:
#         return [i, j]
#   return [-1, -1]

# # Example usage
# nums = [2, 7, 11, 15]
# target = 13
# indices = twoSum_brute_force(nums, target)
# print(indices)

