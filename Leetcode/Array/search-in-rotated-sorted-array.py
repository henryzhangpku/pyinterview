class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i,j=0,n-1 
        while i<=j: #beginning meets the ending index
            m=(i+j)//2
            if nums[m]==target:
                return m
            if nums[i]<=nums[m]: #left is sorted
                if nums[i]<=target<nums[m]: #target is in left
                    j=m-1 #discard right, classic Binary Search
                else:
                    i=m+1 #target is not in left
            else: #right is sorted
                if nums[m]<target<=nums[j]:  #target is in right
                    i=m+1 #discard left , classic Binary Search
                else:
                    j=m-1 #target is not in right
        return -1 #not found



       
                
                