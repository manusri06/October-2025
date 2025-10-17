class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        def rec(index):
            if index == len(nums):
                return [[]]
            
            s = rec(index+1)
            s1 = []
            for i in s:
                s1.append([nums[index]]+i)
            return s1+s
        res = rec(0)

        ans = []

        for i in res:
            if i not in ans:
                ans.append(i)
        return ans
