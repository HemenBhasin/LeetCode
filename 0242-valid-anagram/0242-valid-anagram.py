class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        sarr=[]    
        tarr=[]
        for i in range(len(s)):
            sarr.append(s[i])
        for i in range(len(t)):
            tarr.append(t[i])
        sarr.sort()
        tarr.sort()
        for i in range(len(sarr)):
            if sarr[i]!=tarr[i]:
                return False
        return True        