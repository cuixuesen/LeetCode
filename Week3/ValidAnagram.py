class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Method One
        mapping = {}
        
        for T in t:
            mapping[T] = mapping.get(T,0) + 1
        
        for S in s:
            if S not in mapping:
                return False
            mapping[S] -= 1
            if mapping[S] == 0:
                del mapping[S]
            
        return True if not mapping else False
         
        """
        return all([s.count(c) == t.count(c) for c in set(s+t)])
        """