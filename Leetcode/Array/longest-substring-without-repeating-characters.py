class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        ht={}
        i=0 #beginning index
        for j,x in enumerate(s): #ending index
            if x in ht:
                i=max(ht[x],i)
            ans=max(ans, j-i+1)
            ht[x]=j+1

        return ans