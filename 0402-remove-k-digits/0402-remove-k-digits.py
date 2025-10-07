class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k != 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        if k > 0:
            stack = stack[:-k]
        ans = ''.join(stack).lstrip('0') 
        
        return ans if len(ans) > 0 else '0'
