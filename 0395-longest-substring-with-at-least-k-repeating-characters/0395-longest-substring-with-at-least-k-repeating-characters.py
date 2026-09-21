class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        c=Counter(s)
        for char, count in c.items():
            if count<k:
                return max(self.longestSubstring(s,k) for s in s.split(char))
        return len(s)        
