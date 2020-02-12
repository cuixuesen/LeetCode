class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        
        my = min(strs,key=len)
        if my == "":
            return ""
        strs.remove(my)
        for i, item in enumerate(my):
            for other in strs:
                if other[i] != item:
                    if i == 0:
                        return ""
                    return my[:i]
        return my