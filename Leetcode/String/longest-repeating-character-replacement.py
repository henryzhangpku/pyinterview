class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0 
        i=0 #beginning index
        c=Counter()
        for j,x in enumerate(s): #ending index
            c.update(x) #update counter for frequency
            m=c.most_common()[0][1] #most common count
            #assume keeping m to maximize repeating chareactoer 
            if j-i+1-m>k: #if we are not able to replace the rest within the k operation 
                c.subtract(s[i]) #remove beginning index i from the window
                i+=1 #updating the beginning index
            ans=j-i+1 #distance between ending and begining index 
        return ans


