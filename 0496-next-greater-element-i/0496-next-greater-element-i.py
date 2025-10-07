class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stack=[]
        nums2 = nums2[::-1]
        for i in nums2:
            while stack and stack[-1] <= i:
                stack.pop()
            if not stack:
                dict[i] = -1
            else:
                dict[i] = stack[-1]
            stack.append(i)

        res = []
        for i in nums1:
            res.append(dict[i])
        return res
