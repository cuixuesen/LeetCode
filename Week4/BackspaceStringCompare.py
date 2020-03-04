class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def remove(L):
            i = 0
            while i < len(L):
                if L[i] == "#":
                    if i > 0:
                        del L[i]
                        del L[i-1]
                        i -= 1
                    else:
                        del L[i]
                    
                else:
                    i += 1  
            return "".join(L)
        
        return remove(list(S)) == remove(list(T))
        