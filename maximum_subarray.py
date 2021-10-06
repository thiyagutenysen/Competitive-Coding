class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum<0:
                cur_sum=0
            cur_sum+=nums[i]
            ans = max(ans, cur_sum)
        return ans
        