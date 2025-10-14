class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        maxi = 0
        st = [-1]
        for i,ch in enumerate(s):
            if ch == '(':
                st.append(i)
            
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    maxi = max(maxi, i-st[-1])
        return maxi
