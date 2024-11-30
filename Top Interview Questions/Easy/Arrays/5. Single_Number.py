class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] == nums [1]:
                return nums[0]
        else:
            solution = 0
            for num in nums:
                solution ^= num
            return solution