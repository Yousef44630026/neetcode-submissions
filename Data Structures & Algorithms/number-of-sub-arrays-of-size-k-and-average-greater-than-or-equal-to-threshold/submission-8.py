class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
       l=0
       m=0
       while l+k<=len(arr):
        if sum(arr[l:l+k])>=k*threshold:
            m+=1
        l+=1
       return m     


        