"""class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False"""

class Solution:
    def containsDuplicate(self,nums: List[int]) -> bool:
        s=set()
        for x in nums:
            if x in s:
                return True
            
            s.add(x)
        return False
        