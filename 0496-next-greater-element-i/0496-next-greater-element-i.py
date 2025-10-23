class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
    
        d = {}
        for i in range(len(n2)):
            for j in range(i,len(n2)):
                if n2[i] < n2[j]:
                    d[n2[i]] = n2[j]
                    break
        for i in range(len(n1)):
            if n1[i] in d:
                n1[i] = d[n1[i]]
            else:
                n1[i] = -1
        return n1
                
            