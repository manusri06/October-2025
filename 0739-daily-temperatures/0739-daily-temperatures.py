class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0]*n

        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                index = st.pop()
                res[index] = i-index
            st.append(i)
        return res
                
