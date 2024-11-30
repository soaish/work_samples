class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = "".join(map(str, digits))
        num = str(int(num) + 1)
        return [int(char) for char in num]