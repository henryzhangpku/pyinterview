class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort() #nlog(n)
        ans=[] #(x,y,z) x+y+z =0
        for i in range(n-2): #beginning index, n-3,n-2,n-1
            m,j=i+1,n-1 #search the range m..j to find 3sum 
            # 1. sub problem : two sum within m..j ,target to -nums[i]
            # 2. search in sorted m..j range 
            while m<j:
                s=nums[i]+nums[m]+nums[j]
                if s==0:
                    tp=(nums[i], nums[m],nums[j])
                    if tp not in ans:
                        ans.append(tp)
                    m+=1 #move on with middle/ending index
                    j-=1
                elif s>0:  #m..j >0 , discard the big value j
                    j-=1 #reduce j value
                else: #s<0 
                    m+=1 #increase m value
        
        return ans





                



            
            