class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        my_bag = {5:0, 10:0, 20:0}
        
        for bill in bills:
            my_bag[bill] += 1
            if bill == 10:
                if my_bag[5] >= 1:
                    my_bag[5] -= 1
                else:
                    return False
            elif bill == 20:
                if my_bag[5] >= 1 and my_bag[10] >= 1:
                    my_bag[5] -= 1
                    my_bag[10] -= 1
                elif my_bag[5] >= 3:
                    my_bag[5] -= 3
                else:
                    return False
            
        return True