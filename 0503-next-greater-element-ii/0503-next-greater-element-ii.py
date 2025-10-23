class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = nums+nums
        for i in range(len(nums)):
            for j in range(i,len(n)):
                if nums[i] < n[j]:
                    nums[i] = n[j]
                    break
            else:
                nums[i] = -1
        return nums