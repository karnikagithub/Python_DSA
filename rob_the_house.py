def rob_the_hood(nums):

    rob1, rob2 = 0,0

    for n in nums:

        temp = max(n+rob1,rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


nums = [2,7,9,1,1]
print("The Rob the hood: ", rob_the_hood(nums))



def robHood(arr):

    rob1, rob2 = 0,0

    for n in arr:

        temp = max(n+rob1,rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


nums = [2,7,9,1]
print("The Rob the hood: ", robHood(nums))








