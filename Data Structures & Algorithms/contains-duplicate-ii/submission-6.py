class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        while l<len(nums):
            for r in range(1,min(k,len(nums)-1-l)+1):
                if nums[l]==nums[l+r]:
                    return True
            l+=1
        return False            


        