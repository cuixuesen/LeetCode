class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        score, history = 0, []
        
        for op in ops:
            if op == "+":
                score += history[-1] + history[-2]
                history.append(history[-1] + history[-2])
            elif op == "D":
                score += history[-1] * 2
                history.append(history[-1]*2)
            elif op == "C":
                score -= history[-1]
                del history[-1]
            else:
                score += int(op)
                history.append(int(op))
                
        return score
        