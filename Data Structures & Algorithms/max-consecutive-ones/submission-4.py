class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        l=0
        while l<len(nums):
            res=0
            for r in range(len(nums)-l):
                if nums[l+r]:
                    res+=1
                else:
                    break    
            m=max(m,res)
            l+=r+1
        return m          

        
        
        