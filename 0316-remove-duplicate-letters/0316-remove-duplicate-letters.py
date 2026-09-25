class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        
        for idx, char in enumerate(s):
            if not stack:
                stack.append(char)
            elif char in stack:
                continue
            else:
                while stack and char < stack[-1]  :
                    if stack[-1] in s[idx+1:]:
                        x=stack.pop()
                    else:
                        break
                stack.append(char)              
        return ''.join(stack)
