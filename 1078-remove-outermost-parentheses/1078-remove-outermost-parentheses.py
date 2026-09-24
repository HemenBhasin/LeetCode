class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        rs=[]
        bracket=0
        for char in s:
            
            if char==")":
                bracket-=1    
            if bracket>0:
                rs.append(char)
            if char=="(":
                bracket+=1
        return "".join(rs)                
