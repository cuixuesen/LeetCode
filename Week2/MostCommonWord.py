class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        mapping = {}
        #paragraph = [ str(i) for i in paragraph[:-1].lower().split(" ") if str(i) not in banned]
        paragraph = [w for w in re.split(r"\W", paragraph.lower()) if w]
        
        for word in paragraph:
            if word[-1] == ".":
                word = word[:-1]
            if word not in banned:
                mapping[word] = mapping.get(word, 0) + 1
            else:
                mapping[word] = 0
            
        return max(paragraph, key = lambda x: mapping[x])
            
        
        