class Solution:
    def numSteps(self, s: str) -> int:
        ans = list(s)
        count=0
        while len(ans) != 1:
            if ans[-1] == '0':
                ans.pop()
                count+=1
            else:
                ans[-1] = '0'
                carry = '1'
                i = len(ans)-2
                while carry == '1' and i >= 0:
                    if ans[i] == "1":
                        ans[i]= '0'
                        carry ="1"
                        i-=1
                    else:
                        ans[i]='1'
                        carry="0"
                if carry=='1' and i < 0:
                    ans=['1']+ans
                count+=1
        return count