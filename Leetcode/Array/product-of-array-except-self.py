class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # L m R 
        n=len(nums)
        ans=[1]*n
        #L #beginning to end
        for i in range(1,n): #0, 1, R
            ans[i]=ans[i-1]*nums[i-1] #L aggregated
        #R #end to beginning
        R=1 
        for j in range(n-2,-1,-1):  # L n-2 n-1
            R*=nums[j+1] 
            ans[j]=ans[j] * R # L*R for m

        return ans