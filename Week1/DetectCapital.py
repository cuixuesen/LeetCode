class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if not word:
            return True
        
        if word[0].isupper():
            word = word[1:]
            
        return not word or word.isupper() or word.islower()
        
        
        