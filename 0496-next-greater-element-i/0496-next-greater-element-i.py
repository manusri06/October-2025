class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stack=[]
        for i in nums2:
            while stack and stack[-1] < i:
                e = stack.pop()
                dict[e] = i
            stack.append(i)
        
        for i in range(len(nums1)):
            if nums1[i] in dict:
                nums1[i] = dict[nums1[i]]
            else:
                nums1[i] = -1
        return nums1
