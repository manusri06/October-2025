class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        len_s = len(s)
        i = 0
        while i<len_s:
            if st:
                if st[-1] == s[i]:
                    st.pop()
                else:
                    st.append(s[i])
            
            else:
                st.append(s[i])
            i+=1
        return "".join(st)
            