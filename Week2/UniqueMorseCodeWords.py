class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        mapping = { "a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.." }
        
        myset={}
        result = 0
        for item in words:
            temp_morse=""
            for i in item:
                temp_morse += mapping[i]
            if temp_morse not in myset:
                myset[temp_morse]=1
                result += 1
        return result