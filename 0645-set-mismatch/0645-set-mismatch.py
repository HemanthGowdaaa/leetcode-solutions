class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        result = [0,0]
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for i in range(1,len(nums)+1):
            if i not in count:
                result[1] = i
            if i in  count and count[i] == 2:
                result[0]= i


        return result