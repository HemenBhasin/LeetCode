class Solution(object):
    def reverseOnlyLetters(self, s):
        i=0
        j=len(s)-1
        s=list(s)
        while True:
            if i>=j:
                break
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
            elif not s[i].isalpha():
                i += 1
            
            else:
                j -= 1
        
        return ''.join(s)    

        