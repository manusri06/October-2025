class Solution(object):
    def largestRectangleArea(self, heights):
        
        st = []
        maxarea = 0
        for i,h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                idx , h1 = st.pop()
                maxarea = max(maxarea,h1*(i-idx))
                start = idx
            st.append((start,h))

        n = len(heights)
        for inx,h in st:
            maxarea = max(maxarea,h*(n-inx))
        return maxarea