class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,m,j=0,0,n-1 #beginning ,middle , ending index
        while m<=j:
            if nums[m]==0: #  x<->0 y ,swap 0 to beginning
                nums[i],nums[m]=nums[m],nums[i]
                i+=1
                m+=1
            elif nums[m]==2: # x 2<->y, swap 2 to end
                nums[j],nums[m]=nums[m],nums[j]
                j-=1
            else: # x 1 y, process next middle index
                m+=1
        return nums

            
        