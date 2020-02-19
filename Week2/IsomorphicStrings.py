class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        set_s, set_t = {}, {}
        
        for i,S in enumerate(s):
            set_s[S] = set_s.get(S,[]) + [i]
            
        for i,T in enumerate(t):
            set_t[T] = set_t.get(T,[]) + [i]
            
        return sorted(set_s.values()) == sorted(set_t.values())
            
        
            
        
        
        