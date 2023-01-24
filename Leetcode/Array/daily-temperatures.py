class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T=temperatures
        n=len(T)
        ans=[0]*n
        s=[] #stack 
        for j in range(n):
            while s and T[j]>T[s[-1]]: #warmer/bigger
                i=s[-1] #beginning index , smallest number in stack 
                ans[i]=j-i #update ans with first warmer number
                s.pop() #process next small number
            if not s or T[j]<=T[s[-1]]: #colder/smaller
                s.append(j) #smaller and smaler numbers
        return ans
     