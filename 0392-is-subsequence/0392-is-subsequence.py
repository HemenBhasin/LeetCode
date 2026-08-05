class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        st=list(s)
        for i in range(len(t)):
            if st and st[0]==t[i]:
                st.pop(0)
        return len(st)==0    