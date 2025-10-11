import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        re=r
        while l<=r:
            mid=(l+r)//2
            ho=0
            for p in piles:
                ho+=math.ceil(p/mid)
            if ho<=h:
                re=mid
                r=mid-1
            else:
                l=mid+1
        return re