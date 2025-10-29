class Solution:
    def simplifyPath(self, path: str) -> str:

        st = []
        for i in path.split("/"):
            if i == "..":
                if st:
                    st.pop()
            elif i and i != ".":
                st.append(i)
        return "/" + "/".join(st)

