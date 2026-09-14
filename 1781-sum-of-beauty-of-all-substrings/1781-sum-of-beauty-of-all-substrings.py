class Solution:
    def beautySum(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            arr = [0]*26
            for j in range(i,len(s)):
                arr[ord(s[j]) - ord('a')] += 1
                beauty = max(arr)-min(x for x in arr if x > 0)
                total+=beauty
        return total
                
        