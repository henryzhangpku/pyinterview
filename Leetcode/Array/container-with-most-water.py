class Solution:
    def maxArea(self, height: List[int]) -> int:
        H=height
        n=len(H)
        i,j=0,n-1 #beginning,ending index
        ans=0
        #edge case
        if n==2:
            return min(H[0],H[1])*1 #minimum height 
        #two pointer to find the optimal result
        while i!=j:
            s=min(H[i],H[j]) * (j-i) #mininum height * distance of i,j 
            ans=max(ans, s)
            #advance begining/ending index
            if H[i]<H[j]:
                i+=1 #advance beginning index for higher height 
            else: #H[i]>H[j]
                j-=1 #advance ending index for higher height 
        return ans