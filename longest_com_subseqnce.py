def longest_common_subsequnce(str1,str2):

    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    # print(dp)


    for i in range(len(str1) -1,-1,-1):
        for j in range(len(str2) -1,-1,-1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])

    return dp[0][0]



print(longest_common_subsequnce('abcd','ace'))





def lcs(s1,s2):

    dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    # print(dp)


    for i in range(len(s1) -1, -1, -1):
        for j in range(len(s2) -1,-1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])

    return dp[0][0]


print(lcs('abcd','ace'))
print(lcs('a','ace'))












def lengthOfLIS(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test the function
nums = [10, 9, 2, 5, 3, 101, 18]
print(lengthOfLIS(nums))  # Output: 4