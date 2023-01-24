from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht=defaultdict(list) # k=>[]
        for s in strs:
            a=sorted(s) #array of sorted characters
            k=''.join(a) #sorted key
            ht[k].append(s)
        #k1=[A], k2=[B] =>[[A],[B]]
        return ht.values()  #[[A],[B]]