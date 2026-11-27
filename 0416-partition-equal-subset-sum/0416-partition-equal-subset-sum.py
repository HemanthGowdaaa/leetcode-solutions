class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total//2
        dp = [False] * (target+1)
        dp[0]= True
        for num in nums:
            for sub in range(target,num-1,-1):
                if sub-num >=0:
                    dp[sub]=dp[sub] or dp[sub-num]
        return dp[target]