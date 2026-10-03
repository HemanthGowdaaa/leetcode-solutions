
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = collections.deque()
        res = []
        for right in range(len(nums)):
            while q and q[0] <= right - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            q.append(right)
            if right >= k-1:
                res.append(nums[q[0]])
        return res
        