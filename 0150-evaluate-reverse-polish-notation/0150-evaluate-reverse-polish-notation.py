class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                st.append(int(i))
            else:
                f = st.pop()
                s = st.pop()
                if i == '+':
                    st.append(s+f)
                elif i == '-':
                    st.append(s-f)
                elif i == '*':
                    st.append(s*f)
                elif i == '/':
                    st.append(int(s/f))
        return st[0]
