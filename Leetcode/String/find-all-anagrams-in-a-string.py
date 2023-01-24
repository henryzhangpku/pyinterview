from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        ans=[] #starting index matching to anagram of p
        #easy detech two strings are anagram? 
        #same length , sorted(s1)==sorted(s2)
        c= Counter(p) #hash table to count frequency of each character O(1)
        for i in range(n-m+1): #ending index, n-m+1, last substring has the length of m
            c2=Counter(s[i:i+m])
            if c==c2: #anagram
                ans.append(i)
        return ans
