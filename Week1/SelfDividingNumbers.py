class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        selfDividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return filter(selfDividing, range(left, right + 1))
        