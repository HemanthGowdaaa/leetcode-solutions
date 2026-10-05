class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for _ in range(32):
            bits = n & 1
            rev = rev * 2 + bits
            n = n>>1
        return rev
        