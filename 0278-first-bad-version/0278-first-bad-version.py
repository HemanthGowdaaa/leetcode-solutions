# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n-1
        answer = n
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid) ==  False:
                left = mid+1
            else:
                answer = mid
                right = mid-1
        return answer
        