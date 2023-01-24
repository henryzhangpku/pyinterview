class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      ans=float("inf")
      i=0 #beginning index
      s=0
      for j,x in enumerate(nums): #ending index, value
          s+=x
          while s>=target: 
              ans=min(ans,j-i+1) #updating minimal length
              s-=nums[i] #remove beginning value from sum to reduce the sum for further checking
              i+=1 #updating beginning index

      return ans if ans!=float("inf") else 0

                