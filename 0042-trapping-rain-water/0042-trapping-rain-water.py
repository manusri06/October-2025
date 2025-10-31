class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        water = 0

        for i,curr in enumerate(height):
            while st and height[st[-1]] < curr:
                top = st.pop()

                if not st:
                    break
                d = i-st[-1]-1
                w = min(height[st[-1]],curr) - height[top]
                water += d*w
            st.append(i)
        return water
