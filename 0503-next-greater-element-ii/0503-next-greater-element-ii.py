class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        res = [-1]*n
        
        for i in range(2*n):
            index = i%n
            while st and nums[st[-1]] < nums[index]:
                res[st.pop()] = nums[index]
            st.append(index)
        return res
                