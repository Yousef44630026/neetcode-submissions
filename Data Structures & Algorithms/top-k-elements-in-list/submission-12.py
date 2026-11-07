class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            hashmap[num]=1+hashmap.get(num,0)

        L=[] 
        for num,freq in hashmap.items():
            L.append([freq,num])
        L.sort()   

        res=[]
        while len(res)<k:
            res.append(L.pop()[1])
        return res    









        