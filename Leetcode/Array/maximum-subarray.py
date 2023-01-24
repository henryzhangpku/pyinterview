class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float("-inf")
        s=0
        for x in nums:
           s=max(s+x, x) #new sum to start with
           ans=max(ans, s)
        
        return ans