class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        st = []
        for i in range(2*n):
            index = i%n
            while st and nums[st[-1]] < nums[index]:
                prev = st.pop()
                res[prev] = nums[index]
            if i < n :
                st.append(index)
        return res