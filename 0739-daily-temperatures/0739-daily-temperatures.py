class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []

        for right in range(n):
            while stack and temperatures[stack[-1]] < temperatures[right]:
                left = stack.pop()
                result[left] = right - left
            stack.append(right)
        return result

        