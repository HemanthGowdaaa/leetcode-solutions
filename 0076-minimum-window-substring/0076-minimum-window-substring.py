class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need,window = {},{}

        for ch in t:
            need[ch] = need.get(ch,0)+1
        have,required = 0,len(need)
        left = 0
        best_start=0
        best_length = float('inf')
        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in need and need[s[right]] == window[s[right]]:
                have+=1

            while have == required:
                
                curr = right-left+1
                if curr < best_length:
                    best_start = left
                    best_length = curr

                left_char = s[left]
                window[left_char]-=1
                if left_char in t and need[left_char]> window[left_char]:
                    have-=1
                left+=1
        if best_length == float('inf'):
            return ""
        return s[best_start:best_start+best_length]