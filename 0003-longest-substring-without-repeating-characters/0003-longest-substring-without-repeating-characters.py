class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    count=max(count,j-i+1)    
        return count            