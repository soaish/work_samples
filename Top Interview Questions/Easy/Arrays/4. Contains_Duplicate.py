class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        result = False
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                result = True
                break
            
        return result