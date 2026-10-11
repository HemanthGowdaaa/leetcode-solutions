class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        hmap,arr={},[]
        for i in range(len(speed)):
            hmap[position[i]]=speed[i]
        for pos in sorted(position)[::-1]:
            arr.append([pos,hmap[pos]])
        stack = []
        for pos,spd in arr:
            stack.append((target - pos ) / spd)
            if len(stack) >= 2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)