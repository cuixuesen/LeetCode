class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        digits = [ str(s) for s in digits ]
        num = str(int("".join(digits)) + 1)
        
        return list(num)
        """
        if digits == [9]:
            return [1,0]
        if digits[-1] + 1 == 10:
            digits[-1] = 0
            for i in range(1,len(digits)):
                if digits[-1-i] + 1 == 10:
                    digits[-1-i] = 0
                    if 1+i == len(digits):
                        digits.insert(0,1)
                else:
                    digits[-1-i] = digits[-1-i] + 1
                    break
                
        else:
            digits[-1] = digits[-1] + 1
            
        return digits