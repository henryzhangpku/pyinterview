class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=float("-inf")
        s,t=1,1
        for x in nums:
            if x<0: #flipping sign
                s,t=t,s #swap max with min
            s=max(s*x, x) #max product times x, or new max product starts with x
            t=min(t*x, x) #min product times x, or new min product starts with x
            ans=max(ans, s)
        return ans


