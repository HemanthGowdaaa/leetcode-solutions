class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_seen = {letter:i for i, letter in enumerate(s)}
        seen = set()

        for i, letter in enumerate(s):
            if letter not in seen:
                while stack and stack[-1] > letter and last_seen[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(letter)
                stack.append(letter)
        return "".join(stack)
