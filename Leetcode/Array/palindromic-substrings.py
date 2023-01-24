class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0 #count number of palindrome substrings
        n=len(s)
        # i-1 i (m) j j+1  odd
        # i-1 i (m m+1) j j+1 even
        for m in range(len(s)): #middle index
            for i,j in [(m,m), (m,m+1)]:#odd or even
                while i>=0 and j<n and s[i]==s[j]: #palindromic feature
                    i-=1 #expand the palindrome
                    j+=1
                ans += (j-i)//2 #add the count of palindrome substrings
        return ans