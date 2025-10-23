class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0]*n

        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                res[st.pop()] = i-st[-1]
            st.append(i)
        return res
                
