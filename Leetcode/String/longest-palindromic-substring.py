class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans='' 
        for m in range(n): #middle index 
            #odd i,m,j
            #even i,m,m+1,j
            for i,j in [(m,m),(m,m+1)]: #two pointers
                while 0<=i and j<n and s[i]==s[j]:
                    i-=1 #expanding the palindromic
                    j+=1
                if j-i>len(ans):
                    ans=s[i+1:j] #i,j broken condision,  i+1,j-1 valid palindromic
        return ans
        