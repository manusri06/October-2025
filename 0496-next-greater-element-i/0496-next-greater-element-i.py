class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        d = {}
        s = []
        for i in n2:
            while s and s[-1] < i:
                d[s.pop()] = i
            s.append(i)
            
        res = []
        for i in n1:
            if i in d:
                res.append(d[i])
            else:
                res.append(-1)
        return res
