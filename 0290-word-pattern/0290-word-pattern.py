class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.strip().split()
        if len(pattern)!=len(words):
            return False

        
        for i in range(len(words)):
            if pattern.find(pattern[i])!= words.index(words[i]):
                return False
        return True        
        
            