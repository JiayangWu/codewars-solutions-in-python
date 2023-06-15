def max_sequence(nums):
    if not nums:
        return 0
    if all(num < 0 for num in nums):
        return 0
    dp = [num for num in nums]

    res = nums[0]
    for i, num in enumerate(nums):
        if i: 
            if dp[i - 1] > 0:
                dp[i] = max(dp[i], num + dp[i - 1])
        res = max(dp[i], res)

    return res